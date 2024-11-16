
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Position, Candidate, Voter, Vote
from .forms import VoterRegistrationForm
from .forms import CandidateForm
from .forms import CandidateForm

def home(request):
    return render(request, 'home.html')
def register(request):
    if request.method == 'POST':
        form = VoterRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voter_login')  # Updated to match URL pattern name
    else:
        form = VoterRegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']  # Assuming you have updated your form to use email
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)  # Use email as username

        if user is not None:
            login(request, user)
            return redirect('candidates_list')  # Redirect to candidates list after login
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    return render(request, 'login.html')


def vote(request):
    if request.method == 'POST':
        candidate_id = request.POST.get('candidate_id')
        Vote.objects.create(voter=request.user.voter, candidate_id=candidate_id)
        return redirect('vote_success')  # Define this URL as needed
    candidate_id = request.GET.get('candidate_id')

    candidate = Candidate.objects.get(id=candidate_id) if candidate_id else None
    return render(request, 'vote.html', {'candidate': candidate})


def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:  
            login(request, user)
            return redirect('/admin/')  
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid username or password.'})
    
    return render(request, 'admin_login.html')
def admin_dashboard(request):
    total_voters = Voter.objects.count()
    total_candidates = Candidate.objects.count()
    total_votes = Vote.objects.count()
    # You can add logic for creating charts here
    return render(request, 'admin_dashboard.html', {
        'total_voters': total_voters,
        'total_candidates': total_candidates,
        'total_votes': total_votes,
    })


def candidates_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidates.html', {'candidates': candidates})

def positions_list(request):
    positions = Position.objects.all()
    return render(request, 'positions.html', {'positions': positions})

def add_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')  # or wherever you want to redirect after saving
    else:
        form = CandidateForm()
    
    positions = Position.objects.all()  # Ensure you pass the positions if needed
    return render(request, 'add_candidate.html', {'form': form, 'positions': positions})




