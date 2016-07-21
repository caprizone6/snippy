from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.utils import timezone
from django.core.context_processors import csrf
from forms import FileForm
from models import CSVFile
from django.contrib.auth.decorators import login_required
import vcf
import re
import requests
import csv
import json
from requests.exceptions import ConnectionError
from django.core.files import File

def file_form(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404;
    if request.POST:
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            # read CSV file and define parameters
            input_file_name = re.search(r'/(media/.*)', instance.file.url)
            fileID = instance.id
            input_file = vcf.Reader(open(input_file_name.group(1), "r"))
            output_somatic_file = open('media/somatic_mutation-'+str(fileID)+'.tsv', 'wb')
            output_germline_file = open('media/germline_mutation-'+str(fileID)+'.tsv', 'wb')
            logs = open('media/logs-'+str(fileID)+'.txt', 'w')
            somatic_mutation_array = []
            germline_mutation_array = []

            # Read vcf file and create seperate arrays for somatic and germline mutation
            for record in input_file:
                chr = re.search(r'chr(.*)', str(record.CHROM))
                start_pos = str(record.POS)
                if record.REF == '-':
                    end_pos = record.POS + 1
                else:
                    end_pos = start_pos
                ref = str(record.REF)
                alt = re.search(r'\[(.*)\]', str(record.ALT))
                oncoTator = 'http://www.broadinstitute.org/oncotator/mutation/' + chr.group(
                    1) + '_' + start_pos + '_' + end_pos + '_' + ref + '_' + alt.group(1)
                try:
                    oncoTator_response = requests.get(oncoTator)
                except ConnectionError as e:
                    print e
                    logs.write(str(e))
                    oncoTator_response = "No response"
                if oncoTator_response != "No response":
                    mutation = json.loads(oncoTator_response.text)
                    if "ERROR" in mutation:
                        logs.write("OncoTator is giving error for url:" + oncoTator + " Error message: " + str(
                            oncoTator_response.text))
                    elif chr.group(1) == 'X' or chr.group(1) == 'Y':
                        germline_mutation_array.append(mutation)
                    else:
                        somatic_mutation_array.append(mutation)
            logs.close()

            # write values from arrays to tsv files
            fieldnames = []
            for key in somatic_mutation_array[0]:
                fieldnames.append(str(key))

            tsv_somatic_file = csv.DictWriter(output_somatic_file, fieldnames=fieldnames, delimiter='\t')
            tsv_somatic_file.writeheader()
            for mutation in somatic_mutation_array:
                tsv_somatic_file.writerow(mutation)
            output_somatic_file.close()

            tsv_germline_file = csv.DictWriter(output_germline_file, fieldnames=fieldnames, delimiter='\t')
            tsv_germline_file.writeheader()
            for mutation in germline_mutation_array:
                tsv_germline_file.writerow(mutation)
            output_germline_file.close()

            fileread = open('media/germline_mutation-'+str(fileID)+'.tsv', 'r')
            TSVfile = File(fileread)
            instance.result.save('media/germline_mutation-'+str(fileID)+'.tsv', TSVfile, save=True)

            return HttpResponseRedirect('/result/')
    else:
        form = FileForm()
    return render(request, 'oncotator/snp_tools.html', {'form': form})

@login_required(login_url='/login/')
def result(request):
    files = CSVFile.objects.all()
    return render(request, 'oncotator/result.html', {'files': files})

def snp_detail(request, id):
    try:
        file = CSVFile.objects.get(id=id)
    except CSVFile.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'oncotator/snpdetail.html', {'file': file})
