import json
import csv
import subprocess

def parse_json(json_data):
    data = json.load(open(json_data,"r"))
    formatted_list=[]
    amount = []
    # Format cost by service
    for bill in data['ResultsByTime']:
        for group in bill.get('Groups'):
            print(group.get('Keys')[0])
            print(group.get('Metrics').get('NetAmortizedCost').get('Amount'))
            data={}
            data['service']=group.get('Keys')[0]
            data['cost']=('{0:.2f}$'.format(float(group.get('Metrics').get('NetAmortizedCost').get('Amount'))))
            formatted_list.append(data)
	    print (formatted_list,amount)
    return formatted_list,amount

# def generate_csv(data_list,name):
#     path = '/tmp'
#     subprocess.call(['chmod', '0777', path])
#     keys = data_list[0].keys()
#     file_name = path+"/"+name
#     with open(file_name, 'w') as output_file:
#         dict_writer = csv.DictWriter(output_file, keys)
#         dict_writer.writeheader()
#         dict_writer.writerows(data_list)
#     return file_name

# def display(file_name):
#     with open(file_name, 'r') as output_file:
#         file_content = output_file.read()
#     return file_content


def lambda_handler():
    formatted_list,amount = parse_json("log.json")
#     csv = generate_csv(formatted_list,"cost.csv")
#     print(display(csv))
lambda_handler()
