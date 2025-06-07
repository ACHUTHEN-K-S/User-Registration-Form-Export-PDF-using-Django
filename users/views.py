from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from .models import User
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=form.cleaned_data['username'])
            return generate_pdf(request, user.id)
    else:
        form = UserRegistrationForm()
    return render(request, 'form.html', {'form': form})

def generate_pdf(request, user_id):
    user = User.objects.get(id=user_id)
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    
    story = []
    story.append(Paragraph("User Registration Details", styles['Title']))
    story.append(Spacer(1, 12))
    
    details = [
        f"Username: {user.username}",
        f"Gender: {user.get_gender_display()}",
        f"Date of Birth: {user.dob}",
        f"Age: {user.age}",
        f"District: {user.district}",
        f"State: {user.state}",
        f"Country: {user.country}",
    ]
    
    for detail in details:
        story.append(Paragraph(detail, styles['Normal']))
        story.append(Spacer(1, 12))
    
    doc.build(story)
    buffer.seek(0)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="user_{user.username}_details.pdf"'
    response.write(buffer.getvalue())
    buffer.close()
    return response