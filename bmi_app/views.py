from django.shortcuts import render

def index(request):

    result=None
    angle=0

    if request.method=="POST":

        weight=float(request.POST['weight'])
        height=float(request.POST['height'])

        bmi=weight/((height/100)**2)

        if bmi<18.5:
            category="Underweight"
        elif bmi<25:
            category="Normal"
        elif bmi<30:
            category="Overweight"
        else:
            category="Obese"

        result=f"BMI = {round(bmi,2)} ({category})"

        angle=(bmi/40)*180

    return render(request,'index.html',{
        'result':result,
        'angle':angle
    })


def history(request):
    return render(request,"history.html")