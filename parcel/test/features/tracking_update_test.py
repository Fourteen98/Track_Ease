import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestTrackingUpdate:
    def test_tracking_update_api_create(self, client, tracking_update_data):
        response = client.post(reverse('parcel:tracking_update', kwargs={'track_ease_id': tracking_update_data['parcel']}),
                               data=tracking_update_data,
                               content_type='application/json')

        assert response.status_code == 201, "Should create a tracking update record"

    def test_tracking_update_api_create_fails(self, client, tracking_update_data):
        data = tracking_update_data
        data['status'] = ''
        response = client.post(reverse('parcel:tracking_update', kwargs={'track_ease_id': tracking_update_data['parcel']}),
                               data=data,
                               content_type='application/json')

        assert response.status_code == 400, "Should fail to create a tracking update record"

    def test_tracking_update_api_retrieve(self, client, create_tracking_update_record):
        tracking_update = create_tracking_update_record
        response = client.get(reverse('parcel:tracking_update', kwargs={'track_ease_id': tracking_update.parcel_id.__str__()}))
        assert response.status_code == 200, "Should retrieve a tracking update record"
        assert response.json() != {}, "Should retrieve a tracking update record"

    def test_parcel_has_no_tracking_updates(self, client, create_parcel_record):
        parcel = create_parcel_record
        response = client.get(reverse('parcel:tracking_update', kwargs={'track_ease_id': parcel.id.__str__()}))
        assert response.status_code == 404, "Should fail to retrieve a tracking update record"
        assert response.json()['is_error'] is True, "Should fail to retrieve a tracking update record"
        assert response.json()['message'] == 'No tracking updates found', "Should fail to retrieve a tracking update record"

    def test_tracking_update_api_retrieve_fails(self, client):
        response = client.get(
            reverse('parcel:tracking_update', kwargs={'track_ease_id': '1acc2f6a0811482da1538884bf359dcf'}))

        assert response.status_code == 404, "Should fail to retrieve a tracking update record"
        assert response.json()['is_error'] is True, "Should fail to retrieve a tracking update record"
        assert response.json()['message'] == 'Parcel not found', "Should fail to retrieve a tracking update record"
