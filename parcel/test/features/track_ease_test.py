import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestTrackEase:
    def test_track_ease_api_create(self, parcel_data, django_admin_user_client):
        client = django_admin_user_client
        response = client.post(reverse('parcel:track_ease', kwargs={'track_ease_id': 'ABC123'}), data=parcel_data,
                               content_type='application/json')

        assert response.status_code == 201, "Should create a parcel record"

    def test_track_ease_api_create_fails(self, parcel_data, django_admin_user_client):
        data = parcel_data
        data['tracking_number'] = ''
        client = django_admin_user_client
        response = client.post(reverse('parcel:track_ease', kwargs={'track_ease_id': 'ABC123'}), data=parcel_data,
                               content_type='application/json')

        assert response.status_code == 400, "Should fail to create a parcel record"

    def test_track_ease_api_retrieve(self, create_parcel_record, django_admin_user_client):
        parcel = create_parcel_record
        client = django_admin_user_client
        response = client.get(reverse('parcel:track_ease', kwargs={'track_ease_id': parcel.id}))

        assert response.status_code == 200, "Should retrieve a parcel record"
        assert response.json()['id'] == parcel.id.__str__(), "Should retrieve a parcel record"

    def test_track_ease_api_retrieve_fails(self, django_admin_user_client):
        client = django_admin_user_client
        response = client.get(
            reverse('parcel:track_ease', kwargs={'track_ease_id': '1acc2f6a0811482da1538884bf359dcf'}))

        assert response.status_code == 404, "Should fail to retrieve a parcel record"
        assert response.json()['is_error'] is True, "Should fail to retrieve a parcel record"
        assert response.json()['message'] == 'Parcel not found', "Should fail to retrieve a parcel record"

    def test_track_ease_api_put(self, django_admin_user_client, create_parcel_record):
        parcel = create_parcel_record
        client = django_admin_user_client
        data = {
            'tracking_number': 'ABC123',
            'departure_address': 'Kampala',
            'destination_address': 'Nairobi',
            'current_status': 'In Transit',
        }
        response = client.put(reverse('parcel:track_ease', kwargs={'track_ease_id': parcel.id.__str__()}),
                              data=data,
                              content_type='application/json')
        assert response.status_code == 200, "Should update a parcel record"
        assert response.json()['message'] == 'Parcel updated successfully', "Should update a parcel record"

    def test_track_ease_api_put_fails(self, django_admin_user_client, create_parcel_record):
        data = {
            'tracking_number': 'ABC123',
            'departure_address': '',
            'destination_address': 'Nairobi',
            'current_status': 'In Transit',
        }
        client = django_admin_user_client
        response = client.put(reverse('parcel:track_ease', kwargs={'track_ease_id': '1acc2f6a0811482da1538884bf359dcf'}),
                              data=data,
                              content_type='application/json')

        assert response.status_code == 404, "Should fail to update a parcel record"
        assert response.json()['message'] == 'Parcel not found', "Should fail to update a parcel record"

    def test_track_ease_api_patch(self, django_admin_user_client, create_parcel_record):
        parcel = create_parcel_record
        client = django_admin_user_client
        data = {
            'departure_address': 'Kampala',
            'destination_address': 'Nairobi',
            'current_status': 'In Transit',
        }
        response = client.patch(reverse('parcel:track_ease', kwargs={'track_ease_id': parcel.id.__str__()}),
                                data=data,
                                content_type='application/json')
        assert response.status_code == 200, "Should patch a parcel record"
        assert response.json()['message'] == 'Parcel updated successfully', "Should patch a parcel record"

    def test_track_ease_api_patch_fails(self, django_admin_user_client, create_parcel_record):
        parcel = create_parcel_record
        client = django_admin_user_client
        data = {
            'departure_address': 'Kampala',
            'destination_address': 'Nairobi',
            'current_status': 'In Transit',
        }

        response = client.patch(reverse('parcel:track_ease', kwargs={'track_ease_id': '1acc2f6a0811482da1538884bf359dcf'}),
                                data=data,
                                content_type='application/json')

        assert response.status_code == 404, "Should fail to patch a parcel record"
        assert response.json()['message'] == 'Parcel not found', "Should fail to patch a parcel record"

    def test_track_ease_api_delete(self, django_admin_user_client, create_parcel_record):
        parcel = create_parcel_record
        client = django_admin_user_client
        response = client.delete(reverse('parcel:track_ease', kwargs={'track_ease_id': parcel.id.__str__()}))

        assert response.status_code == 204, "Should delete a parcel record"

    def test_track_ease_api_delete_fails(self, django_admin_user_client):
        client = django_admin_user_client
        response = client.delete(
            reverse('parcel:track_ease', kwargs={'track_ease_id': '1acc2f6a0811482da1538884bf359dcf'}))

        assert response.status_code == 404, "Should fail to delete a parcel record"
        assert response.json()['message'] == 'Parcel not found', "Should fail to delete a parcel record"
