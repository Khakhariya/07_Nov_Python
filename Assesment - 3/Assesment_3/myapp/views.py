from django.shortcuts import render, redirect
from .models import signup_model, members_model, events_model, watchmans_model, visitors_model, transactions_model,notices_model
from django.contrib.auth import logout
from .forms import members_form, editmembers_form, signup_update_form, events_form, editevent_form, watchmans_form, editwatchmans_form, visitors_form, visitors_list_form, transactions_form,notices_form,notices_view_form
from django.core.mail import send_mail
from Assesment_3 import settings
from django.contrib import messages

# Create your views here.


def index(request):
    username = request.session.get('username')
    if username is not None:
        return redirect('home')

    if request.method == 'POST':
        
        unm = request.POST['username']
        pas = request.POST['password']

        member = members_model.objects.all()
        user = signup_model.objects.all()
        watchman = watchmans_model.objects.all()

        for i in member:

            if unm == i.username:

                member = members_model.objects.get(username=unm)
                mem_var = members_model.objects.filter(
                    username=unm, password=pas)

                if mem_var:
                    print('LogIn Successfully!')
                    request.session['username'] = unm
                    request.session['userid'] = member.id
                    category = 'Member'
                    request.session['category'] = category

                    return redirect('home')
                else:
                    print('Error! Login Failed')

        for i in user:

            if unm == i.username:

                user = signup_model.objects.get(username=unm)
                user_var = signup_model.objects.filter(
                    username=unm, password=pas)

                if user_var:
                    print('LogIn Successfully!')
                    request.session['username'] = unm
                    request.session['userid'] = user.id
                    category = 'User'
                    request.session['category'] = category

                    return redirect('home')
                else:
                    print('Error! Login Failed')

        for i in watchman:

            if unm == i.username:

                watchman = watchmans_model.objects.get(username=unm)
                watchman_var = watchmans_model.objects.filter(
                    username=unm, password=pas)

                if watchman_var:
                    print('LogIn Successfully!')
                    request.session['username'] = unm
                    request.session['userid'] = watchman.id
                    category = 'Watchman'
                    request.session['category'] = category

                    return redirect('home')
                else:
                    print('Error! Login Failed')

    return render(request, 'index.html')


def forget(request):

    if request.method == 'POST':
        unm = request.POST['username']
        userdata = signup_model.objects.get(username=unm)

        # send mail to user :-

        subject = 'Forget Password'
        message = f'Dear user, \n\nYour password is {userdata.password} \n\nNever Share Your password to any one.'
        mail = settings.EMAIL_HOST_USER
        maillist = [userdata.mail]

        send_mail(subject=subject,message=message,from_email=mail,recipient_list=maillist)

        messages.success(
            request, 'Your Password has been Sent in Your registered E-Mail')

    return render(request, 'forget.html')


def profile(request):

    category = request.session.get('category')

    uid = request.session.get('userid')
    userdata = signup_model.objects.get(id=uid)
    usersignupdata = signup_model.objects.get(id=uid)

    if request.method == 'POST':
        updatedata = signup_update_form(request.POST)
        if updatedata.is_valid():
            updatedata = signup_update_form(
                request.POST, instance=usersignupdata)
            updatedata.save()
            print('Your Data has been updated.')
        else:
            print(updatedata.errors)

    return render(request, 'profile.html', {'userdata': userdata, 'category': category})


def home(request):

    category = request.session.get('category')
    username = request.session.get('username')

    return render(request, 'home.html', {'user': username, 'category': category})


def userlogout(request):

    logout(request)
    print('Logout! Successfully.')

    return redirect('/')

# Society Member :-


def societymember(request):

    category = request.session.get('category')

    if request.method == 'POST':
        mem = members_form(request.POST)
        if mem.is_valid():
            mem.save()
            print('Society Member data has been added successfully.')

        else:
            print(mem.errors)

    return render(request, 'societymember.html', {'category': category})


def editsocietymember(request):

    category = request.session.get('category')
    memberdata = members_model.objects.all()

    if request.method == 'POST':

        Member_id = request.POST.get('id')
        Member_data = members_model.objects.get(id=Member_id)

        memedit = editmembers_form(request.POST)
        if memedit.is_valid():
            memedit = editmembers_form(request.POST, instance=Member_data)
            memedit.save()
            print('Your data has been updated successfully')

        else:
            print(memedit.errors)

    return render(request, 'editsocietymenber.html', {'memberdata': memberdata, 'category': category})


def membermaintenance (request):

    memberdata = []
    square_foot = 0
    per_square_rate = 0
    Total_charges = 0

    category = request.session.get('category')

    # transaction data
    trans_data = transactions_model.objects.all()

    for i in trans_data:

        print(i.rate)
        Ratepersq = i.rate
        maintenance_rate = i.maintenance_rate
        parking = i.parking
        event_fund = i.event_fund

    # user data
    userid = request.session.get('userid')

    if request.method == 'POST':

        memberdata = members_model.objects.get(id=userid)

        if memberdata.bhk == 2:
            square_foot = 700
            per_square_rate = square_foot * Ratepersq

        elif memberdata.bhk == 3:
            square_foot = 850
            per_square_rate = square_foot * Ratepersq

        elif memberdata.bhk == 4:
            square_foot = 1000
            per_square_rate = square_foot * Ratepersq

        Total_charges = per_square_rate + maintenance_rate + parking + event_fund

    return render(request, 'membermaintenance.html',{'category': category, 'trans_data': trans_data, 'memberdata': memberdata, 'per_square_rate': per_square_rate, 'Total_charges': Total_charges,'userid':userid})


def memberevents(request):

    category = request.session.get('category')

    eventdata = events_model.objects.all()

    return render(request, 'memberevents.html', {'category': category,'eventdata':eventdata})


def deletemember(request, id):

    member_id = members_model.objects.get(id=id)
    member_id.delete()

    messages.error(request, 'Your member has been successfully.')

    return redirect('editsocietymember')

# Society Watchmen :-


def watchmen(request):

    category = request.session.get('category')
    if request.method == 'POST':
        watch_var = watchmans_form(request.POST)
        if watch_var.is_valid():
            watch_var.save()
            print('watchman Added suceesfully')
        else:
            print(watch_var.errors)

    return render(request, 'watchmen.html', {'category': category})


def editwatchmen(request):

    category = request.session.get('category')
    watch_data = watchmans_model.objects.all()

    if request.method == 'POST':

        watch_id = request.POST['id']
        watch_id_data = watchmans_model.objects.get(id=watch_id)

        watch_edit = editwatchmans_form(request.POST)

        if watch_edit.is_valid():
            watch_edit = editwatchmans_form(
                request.POST, instance=watch_id_data)
            watch_edit.save()
            print('watchman data is updated successfully.')
        else:
            print(watch_edit.errors)

    return render(request, 'editwatchmen.html', {'watch_data': watch_data, 'category': category})


def deletewatchman(request, id):

    watchman_id = watchmans_model.objects.get(id=id)
    watchman_id.delete()

    messages.error(request, 'Your member has been successfully.')

    return redirect('editwatchmen')

# Visitors :-


def visitors(request):

    category = request.session.get('category')
    if request.method == 'POST':
        vis_var = visitors_form(request.POST)
        if vis_var.is_valid():
            vis_var.save()
            print('visitor Details Entered successfully.')
            messages.success(request, 'visitor Details Entered successfully.')
        else:
            print(vis_var.errors)

    return render(request, 'visitors.html', {'category': category})


def visitors_list(request):

    category = request.session.get('category')
    vis_data = visitors_model.objects.all()

    if request.method == 'POST':

        vis_id = request.POST['id']
        vis_id_data = visitors_model.objects.get(id=vis_id)

        vis_var = visitors_list_form(request.POST)
        if vis_var.is_valid():
            vis_var = visitors_list_form(request.POST, instance=vis_id_data)
            vis_var.save()
            print('visitor Out time entered successfully.')
            messages.success(request, 'visitor Out time entered successfully.')
        else:
            print(vis_var.errors)

    return render(request, 'visitor_list.html', {'vis_data': vis_data, 'category': category})

def deletevisitor (request,id):

    visitors_id = visitors_model.objects.get(id=id)
    visitors_id.delete()

    messages.error(request, 'Your Event has been deleted successfully.')

    return redirect('visitor')

# Events :-


def events(request):

    category = request.session.get('category')
    if request.method == 'POST':
        eve = events_form(request.POST, request.FILES)
        if eve.is_valid():
            eve.save()
            print('event is updated successfully.')
            messages.success(request, 'event is updated successfully.')
        else:
            print(eve.errors)

    return render(request, 'Events.html', {'category': category})


def editevent(request):
    
    category = request.session.get('category')
    eventdata = events_model.objects.all()

    if request.method == 'POST':

        event_id = request.POST.get('id')
        event_data = events_model.objects.get(id=event_id)

        eveedit = editevent_form(request.POST, request.FILES)
        if eveedit.is_valid():
            eveedit = editevent_form(
                request.POST, request.FILES, instance=event_data)
            eveedit.save()
            print('Your data has been updated successfully')

        else:
            print(eveedit.errors)

    return render(request, 'editevent.html', {'eventdata': eventdata, 'category': category})


def deleteevent(request, id):

    event_id = events_model.objects.get(id=id)
    event_id.delete()

    messages.error(request, 'Your Event has been deleted successfully.')

    return redirect('editevent')

# Notices :-


def notices(request):
    
    category = request.session.get('category')

    if request.method == 'POST':
        notice = notices_form(request.POST, request.FILES)
        if notice.is_valid():
            notice.save()
            print('Notice is Added successfully.')
            messages.success(request, 'Notice is Added successfully.')
        else:
            print(notice.errors)

    return render(request, 'notices.html', {'category': category})


def notice_view(request):

    category = request.session.get('category')
    noticedata = notices_model.objects.all()

    if request.method == 'POST':

        notice_id = request.POST.get('id')
        notice_data = notices_model.objects.get(id=notice_id)

        noticeedit = notices_view_form(request.POST, request.FILES)
        if noticeedit.is_valid():
            noticeedit = notices_view_form(request.POST, request.FILES)
            noticeedit.save()
            print('Your data has been updated successfully')

        else:
            print(noticeedit.errors)

    return render(request, 'notice_view.html', {'category': category,'noticedata':noticedata})

def deletenotice (request,id):

    notice_id = notices_model.objects.get(id=id)
    notice_id.delete()

    messages.error(request, 'Your Event has been deleted successfully.')

    return redirect('notice_view')



# transactions :-

def transactions_charges(request):

    category = request.session.get('category')
    id = 0
    trans_data = []
    transaction_data = transactions_model.objects.all()
    for i in transaction_data:
        print(i.id)
        id = i.id
    if id > 0:
        trans_data = transactions_model.objects.get(id=id)
    if request.method == 'POST':
        trans_var = transactions_form(request.POST)
        if trans_var.is_valid():
            if id > 0:
                trans_var = transactions_form(
                    request.POST, instance=trans_data)
            trans_var.save()
            print('Charges added successfully.')
            messages.success(request, 'Charges added successfully.')
        else:
            print(trans_var.errors)
            messages.error(request, trans_var.errors)

    return render(request, 'transaction_charges.html', {'category': category, 'trans_data': trans_data})


def transaction_bill(request):

    memberdata = []
    square_foot = 0
    per_square_rate = 0
    Total_charges = 0

    category = request.session.get('category')

    trans_data = transactions_model.objects.all()

    for i in trans_data:

        print(i.rate)
        Ratepersq = i.rate
        maintenance_rate = i.maintenance_rate
        parking = i.parking
        event_fund = i.event_fund

    if request.method == 'POST':

        memberid = request.POST['id']
        memberdata = members_model.objects.get(id=memberid)

        if memberdata.bhk == 2:
            square_foot = 700
            per_square_rate = square_foot * Ratepersq

        elif memberdata.bhk == 3:
            square_foot = 850
            per_square_rate = square_foot * Ratepersq

        elif memberdata.bhk == 4:
            square_foot = 1000
            per_square_rate = square_foot * Ratepersq

        Total_charges = per_square_rate + maintenance_rate + parking + event_fund

    return render(request, 'transaction_bill.html', {'category': category, 'trans_data': trans_data, 'memberdata': memberdata, 'per_square_rate': per_square_rate, 'Total_charges': Total_charges})
