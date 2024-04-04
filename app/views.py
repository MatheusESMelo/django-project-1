from django.shortcuts import get_object_or_404, render
from app.models import Employee

def employee_detail(request, pk):
    # try:
    #     employee = Employee.objects.get(pk=pk)
    #     print(employee)
    # except:
    #     raise Http404
        employee = get_object_or_404(Employee, pk=pk)
        context = {
            "employee": employee,
        }
        # print(employee)
        return render(request, 'employee_detail.html', context)
