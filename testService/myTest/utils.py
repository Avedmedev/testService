class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        context['authen'] = True if self.request.user.is_authenticated else False
        return context
