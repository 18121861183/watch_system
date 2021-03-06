# Generated by Django 2.1.7 on 2019-03-03 07:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IntelligenceRecord',
            fields=[
                ('key', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='威胁情报关键字')),
                ('tag', models.CharField(max_length=100, verbose_name='威胁标签')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='WebDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_id', models.IntegerField(default=0, verbose_name='网站ID')),
                ('whois_info', models.TextField(verbose_name='whois信息')),
                ('ip_info', models.TextField(verbose_name='ip信息')),
                ('threat_info', models.TextField(verbose_name='威胁信息')),
                ('leak_info', models.TextField(verbose_name='漏洞信息')),
                ('server_info', models.TextField(verbose_name='端口服务')),
            ],
        ),
        migrations.CreateModel(
            name='WebInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_name', models.CharField(max_length=100, verbose_name='网站名称')),
                ('web_url', models.CharField(max_length=200, verbose_name='网站URL')),
                ('status', models.CharField(max_length=100, verbose_name='安全状态，逗号分隔')),
            ],
        ),
    ]
