## djangosite

学习django基础所做的一个练手项目。

### 建立项目
```
django-admin startproject django_project_name
```

#### 建立应用
每个Django项目可能包含多个Django应用
```
python3 manage.py startapp django_app_name
```

### 生成数据库移植文件
```
python3 manage.py makemigrations django_app_name
```

### 移植到数据库
```
python3 manage.py migrate
```

### 创建管理员
```
python3 manage.py createsuperuser
```

### 运行项目
```
python3 manage.py runserver -h localhost -p 8080
```
