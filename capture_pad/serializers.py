from rest_framework import serializers
from .models import Notebook, Year, Month, Day, Note

class NotebookSerializer(serializers.HyperlinkedModelSerializer):
    years = serializers.HyperlinkedRelatedField(
        view_name='api_year_detail',
        many=True,
        read_only=True
    )
    notebook_url = serializers.ModelSerializer.serializer_url_field(
        view_name='api_notebook_detail'
    )

    class Meta:
        model=Notebook
        fields=('id', 'notebook_url', 'title', 'active', 'years')

class YearSerializer(serializers.HyperlinkedModelSerializer):
    months = serializers.HyperlinkedRelatedField(
        view_name='api_month_detail',
        many=True,
        read_only=True
    )
    year_url = serializers.ModelSerializer.serializer_url_field(
        view_name='api_year_detail'
    )
    notebook_id = serializers.PrimaryKeyRelatedField(
        queryset=Notebook.objects.all(),
        source='notebook'
    )

    class Meta:
        model=Year
        fields=('id', 'year_url', 'notebook_id', 'name', 'months')

class MonthSerializer(serializers.HyperlinkedModelSerializer):
    days = serializers.HyperlinkedRelatedField(
        view_name='api_day_detail',
        many=True,
        read_only=True
    )
    month_url = serializers.ModelSerializer.serializer_url_field(
        view_name='api_month_detail'
    )
    year_id = serializers.PrimaryKeyRelatedField(
        queryset=Year.objects.all(),
        source='year'
    )
    class Meta:
        model=Month
        fields=('id', 'month_url', 'year_id', 'name', 'days')

class DaySerializer(serializers.HyperlinkedModelSerializer):
    notes = serializers.HyperlinkedRelatedField(
        view_name='api_note_detail',
        many=True,
        read_only=True
    )
    day_url = serializers.ModelSerializer.serializer_url_field(
        view_name='api_day_detail'
    )
    month_id = serializers.PrimaryKeyRelatedField(
        queryset=Month.objects.all(),
        source='month'
    )
    class Meta:
        model=Day
        fields=('id', 'day_url', 'month_id', 'name', 'date', 'notes')

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    note_url = serializers.ModelSerializer.serializer_url_field(
        view_name='api_note_detail'
    )
    day_id = serializers.PrimaryKeyRelatedField(
        queryset=Day.objects.all(),
        source='day'
    )
    class Meta:
        model=Note
        fields=('id', 'note_url', 'day_id', 'textContent', 'complete', 'date', 'dueDate')