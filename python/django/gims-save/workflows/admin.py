from django.contrib import admin

# Register your models here.
from .models import Workflows, WorkflowType, LabWorkFlows, LabWorkFlowStatus, LabWorkFlowType


class WorkflowsAdmin(admin.ModelAdmin):
    list_display = ['type', 'name', 'workflow_id', 'version','inputs','status']

    def queryset(self, request):
        return Workflows.wf_objects


class WorkflowTypeAdmin(admin.ModelAdmin):
    list_display = ['type', 'type_name']


class LabWorkflowTypeAdmin(admin.ModelAdmin):
    list_display = ['type', 'type_name']


class LabWorkFlowStatusAdmin(admin.ModelAdmin):
    list_display = ['status', 'workflow','order', 'sample', 'result']


class LabWorkFlowsAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date', 'type', 'samples_list', 'status']

admin.site.register(WorkflowType, WorkflowTypeAdmin)
admin.site.register(Workflows, WorkflowsAdmin)
admin.site.register(LabWorkFlowStatus, LabWorkFlowStatusAdmin)
admin.site.register(LabWorkFlowType, LabWorkflowTypeAdmin)
admin.site.register(LabWorkFlows, LabWorkFlowsAdmin)