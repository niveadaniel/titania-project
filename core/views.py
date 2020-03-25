from django.shortcuts import render, redirect
from .models import Owner, OwnerContractType, OwnerSituation, Tower, VehicleType, Notification
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import datetime

def index(request):
    return redirect('/login/')


def login(request):
    return render(request, 'login.html')


def list_residents(request):
    towers = Tower.objects.all()
    dic = {'towers': towers}
    return render(request, 'list_residents.html', dic)


def edit_resident(request):
    print(request.GET)
    towers = Tower.objects.all()
    contract_types = OwnerContractType.objects.all()
    situations = OwnerSituation.objects.all()
    vehicle_types = VehicleType.objects.all()
    owner_id = request.GET.get('id')
    if owner_id:
        owner = Owner.objects.get(id=owner_id)
    else:
        owner = None
    dic = {'owner': owner, 'towers': towers, 'contract_types': contract_types, 'situations': situations, 'vehicle_types': vehicle_types}
    return render(request, 'edit_resident.html', dic)


@csrf_exempt
def save_resident(request):
    print(request.POST)
    owner_id = request.POST['id']
    owner_name = request.POST['owner_name']
    tower = request.POST['tower']
    apartment = request.POST['apartment']
    residents = request.POST['amount_residents']
    contract_type = request.POST['contract_type']
    situation = request.POST['situation']
    phone_number = request.POST['phone_number']
    cell_phone = request.POST['cell_phone']
    email = request.POST['email']
    vehicle_type_1 = request.POST['vehicle_type']
    vehicle_brand_1 = request.POST['vehicle_brand']
    vehicle_model_1 = request.POST['vehicle_model']
    license_plate_1 = request.POST['license_plate']
    vehicle_type_2 = request.POST['vehicle_type_2']
    vehicle_brand_2 = request.POST['vehicle_brand_2']
    vehicle_model_2 = request.POST['vehicle_model_2']
    license_plate_2 = request.POST['license_plate_2']
    notes = request.POST['note']
    print(owner_id)

    if owner_id:
        owner = Owner.objects.filter(id=owner_id).update(name=owner_name, tower_id=tower,
                                                         apartment=apartment,
                                                         residents=residents,
                                                         contract_type_id=contract_type,
                                                         situation_id=situation,
                                                         phone_number=phone_number,
                                                         cell_phone=cell_phone,
                                                         email=email,
                                                         vehicle_type_1_id=vehicle_type_1,
                                                         vehicle_brand_1=vehicle_brand_1,
                                                         vehicle_model_1=vehicle_model_1,
                                                         license_plate_1=license_plate_1,
                                                         vehicle_type_2_id=vehicle_type_2,
                                                         vehicle_brand_2=vehicle_brand_2,
                                                         vehicle_model_2=vehicle_model_2,
                                                         license_plate_2=license_plate_2,
                                                         notes=notes)
        owner = Owner.objects.get(id=owner_id)
    else:
        owner = Owner.objects.create(name=owner_name, tower_id=tower,
                                     apartment=apartment,
                                     residents=residents,
                                     contract_type_id=contract_type,
                                     situation_id=situation,
                                     phone_number=phone_number,
                                     cell_phone=cell_phone,
                                     email=email,
                                     vehicle_type_1_id=vehicle_type_1,
                                     vehicle_brand_1=vehicle_brand_1,
                                     vehicle_model_1=vehicle_model_1,
                                     license_plate_1=license_plate_1,
                                     vehicle_type_2_id=vehicle_type_2,
                                     vehicle_brand_2=vehicle_brand_2,
                                     vehicle_model_2=vehicle_model_2,
                                     license_plate_2=license_plate_2,
                                     notes=notes)

    owner_code = 'AP' + str(owner.apartment) + 'BL' + str(owner.tower)
    owner.owner_code = owner_code
    owner.save()

    return JsonResponse({'success': True, 'id': owner.id, 'message': 'Não foi possivel salvar.'})


def create_data_table_owners(owners):
    owners_list = []
    if owners:
        for owner in owners:
            owners_list.append([owner.tower.number,
                                "<a style='color: #428bca;' href='/edit/resident/?id=%s'>" % str(owner.id) + str(owner.apartment) + "</a>",
                                owner.name,
                                owner.contract_type.name,
                                owner.email])
    return owners_list


@csrf_exempt
def get_owners_list(request):
    print(request.POST)
    tower = request.POST['tower']
    draw = int(request.POST['draw'])
    value = request.POST['search[value]']
    owners = Owner.objects.all()
    if tower:
        owners = owners.filter(tower_id=tower)
    if value:
        owners = owners.filter(Q(tower__number__icontains=value) |
                               Q(apartment__icontains=value) |
                               Q(name__icontains=value) |
                               Q(contract_type__name__icontains=value) |
                               Q(email__icontains=value))
    total = owners.count()
    owners_list = create_data_table_owners(owners)
    return JsonResponse({'draw': draw + 1, 'recordsTotal': total, 'recordsFiltered': total, 'data': owners_list})


@csrf_exempt
def list_notifications(request):
    notifications = Notification.objects.all()
    dic = {'notifications': notifications}
    return render(request, 'list_notifications.html', dic)


@csrf_exempt
def get_notification(request):
    notification_id = request.GET['id']
    notification = Notification.objects.get(id=notification_id)
    dic = {'notification': notification}
    return render(request, 'view_notification.html', dic)


@csrf_exempt
def edit_notification(request):
    notification = None
    if request.GET:
        notification_id = request.GET['id']
        if notification_id:
            notification = Notification.objects.get(id=notification_id)
    dic = {'notification': notification}
    return render(request, 'edit_notification.html', dic)


@csrf_exempt
def save_notification(request):
    notification_id = request.POST['id']
    title = request.POST['title']
    description = request.POST['description']
    notification = request.POST['notification']
    date_now = datetime.datetime.now()
    if notification_id:
        notification = Notification.objects.filter(id=notification_id).update(title=title,
                                                                              description=description,
                                                                              notification=notification)
        notification = Notification.objects.get(id=notification_id)
    else:
        notification = Notification.objects.create(title=title,
                                                   description=description,
                                                   notification=notification,
                                                   created_date=date_now)
        notification.save()

    return JsonResponse({'success': True})


@csrf_exempt
def delete_notification(request):
    notification_id = request.GET['id']
    if notification_id:
        notification = Notification.objects.filter(id=notification_id).delete()
    return list_notifications(request)