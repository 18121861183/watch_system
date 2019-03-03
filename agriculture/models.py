from django.db import models
import django.utils.timezone as timezone


class IntelligenceRecord(models.Model):
    key = models.CharField(max_length=100, verbose_name="威胁情报关键字", primary_key=True)
    tag = models.CharField(max_length=100, verbose_name="威胁标签")
    create_time = models.DateTimeField(verbose_name="更新时间", default=timezone.now)


class WebInfo(models.Model):
    web_name = models.CharField(max_length=100, verbose_name="网站名称")
    web_url = models.CharField(max_length=200, verbose_name="网站URL")
    status = models.CharField(max_length=100, verbose_name="安全状态，逗号分隔")


class WebDetail(models.Model):
    web_id = models.IntegerField(verbose_name="网站ID", default=0)
    whois_info = models.TextField(verbose_name="whois信息")
    ip_info = models.TextField(verbose_name="ip信息")
    threat_info = models.TextField(verbose_name="威胁信息")
    leak_info = models.TextField(verbose_name="漏洞信息")
    server_info = models.TextField(verbose_name="端口服务")


