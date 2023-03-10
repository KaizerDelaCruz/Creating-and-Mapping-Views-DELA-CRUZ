from django.shortcuts import render
from django.http import HttpResponse

def Mission(request):
    return HttpResponse("The College of Computer Studies shall produce technically competent Information Technology professionals adequately prepared in the practice of their profession supportive of national development goals and standars of global excellence.")

def Vision(request):
    return HttpResponse("In 2030, the Manuel S. Enverga University Foundation is a global competitve university with high concentration of talent, excellent teaching environment, rigorous program quality, sufficient resources, and a culture of collaboration.")

def Objectives(request):
    return HttpResponse("1.Be employed and demonstrate professionalism, competence and passion in solving contemporary computing problems by developing or utilizing innovative IT solutions.<br> 2.Embark in lifelong learning or research to attune to the continous innovation in the IT industry in order to adapt to the changing demands of the global market; and<br> 3.Exhibit leadership and teamwork and commitment to their respective local or global organizations. ")