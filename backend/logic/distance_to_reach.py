from apis import google_maps


def update_distance_to_reach(points):
    points[0]["distance_in_meters"] = 0
    points[0]["duration_in_mins"] = 0

    for i in range(1, len(points)):
        origin_place_id = points[i]["details"]["place_id"]
        destination_place_id = points[i - 1]["details"]["place_id"]
        distance_data = google_maps.google_distance_matrix(
            origin_place_id, destination_place_id
        )
        points[i]["distance_in_meters"] = distance_data["distance_in_meters"]
        points[i]["duration_in_mins"] = distance_data["duration_in_mins"]
    return points
