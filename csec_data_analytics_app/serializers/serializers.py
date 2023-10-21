from rest_framework import serializers


class ReferenceSerializer(serializers.Serializer):
    url = serializers.URLField(max_length=500)
    source = serializers.CharField()
    tags = serializers.ListField(child=serializers.CharField())


class CVSSV2Serializer(serializers.Serializer):
    source = serializers.CharField()
    type = serializers.ChoiceField(choices=["Primary", "Secondary"])
    cvssData = serializers.JSONField()  # You might want to create a specific serializer for cvssData
    baseSeverity = serializers.CharField()
    exploitabilityScore = serializers.FloatField()
    impactScore = serializers.FloatField()
    acInsufInfo = serializers.BooleanField()
    obtainAllPrivilege = serializers.BooleanField()
    obtainUserPrivilege = serializers.BooleanField()
    obtainOtherPrivilege = serializers.BooleanField()
    userInteractionRequired = serializers.BooleanField()


class CVSSV3Serializer(serializers.Serializer):
    source = serializers.CharField()
    type = serializers.ChoiceField(choices=["Primary", "Secondary"])
    cvssData = serializers.JSONField()  # You might want to create a specific serializer for cvssData
    exploitabilityScore = serializers.FloatField()
    impactScore = serializers.FloatField()


class CVSSV31Serializer(serializers.Serializer):
    source = serializers.CharField()
    type = serializers.ChoiceField(choices=["Primary", "Secondary"])
    cvssData = serializers.JSONField()  # You might want to create a specific serializer for cvssData
    exploitabilityScore = serializers.FloatField()
    impactScore = serializers.FloatField()


class MetricSerializer(serializers.Serializer):
    cvssMetricV31 = CVSSV31Serializer(many=True)
    cvssMetricV30 = CVSSV3Serializer(many=True)
    cvssMetricV2 = CVSSV2Serializer(many=True)


class DescriptionSerializer(serializers.Serializer):
    lang = serializers.CharField()
    value = serializers.CharField(max_length=4096)


class CVEItemSerializer(serializers.Serializer):
    id = serializers.RegexField(regex=r'^CVE-[0-9]{4}-[0-9]{4,}$')
    published = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")
    lastModified = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")
    evaluatorComment = serializers.CharField()
    evaluatorSolution = serializers.CharField()
    evaluatorImpact = serializers.CharField()
    cisaExploitAdd = serializers.DateField(format="%Y-%m-%d")
    cisaActionDue = serializers.DateField(format="%Y-%m-%d")
    cisaRequiredAction = serializers.CharField()
    cisaVulnerabilityName = serializers.CharField()
    descriptions = DescriptionSerializer(many=True)
    references = ReferenceSerializer(many=True)
    metrics = MetricSerializer()
    weaknesses = serializers.ListField(child=serializers.DictField())  # You might want to create a specific serializer for weaknesses
    configurations = serializers.ListField(child=serializers.DictField())  # You might want to create a specific serializer for configurations
    vendorComments = serializers.ListField(child=serializers.DictField())  # You might want to create a specific serializer for vendorComments
