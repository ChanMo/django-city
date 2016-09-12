Django-city
=======================

一个基于django的城市模块

快速开始:
---------

安装django-city:

.. code-block::

    pip install django-city

修改setttings.py:

.. code-block::

    INSTALLED_APPS = (
        ...
        'city',
        ...
    )

在admin中使用:

.. code-block::
    
    from city.admin import CityAdminMixin

    class DemoAdmin(CityAdminMixin, admin.ModelAdmin):
        pass

在views中使用:

.. code-block::

    from city.views import CityViewMixin

    class DemoView(CityViewMixin):
        pass



版本更改:
---------

v0.0.2 添加`CityViewMixin`
v0.0.1 第一版
