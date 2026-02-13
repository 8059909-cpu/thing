# Camera Monitoring System for FNAF 2 Fan Game

class CameraSystem:
    def __init__(self, camera_count):
        self.camera_count = camera_count
        self.active_cameras = []
        self.camera_feed = []
        self.initialize_cameras()

    def initialize_cameras(self):
        for cam_id in range(1, self.camera_count + 1):
            self.camera_feed.append(f'Camera {cam_id} feed')
        print(f'Initialized {self.camera_count} cameras.')

    def activate_camera(self, cam_id):
        if cam_id not in self.active_cameras:
            self.active_cameras.append(cam_id)
            print(f'Activated Camera {cam_id}.')
        else:
            print(f'Camera {cam_id} is already active.')

    def deactivate_camera(self, cam_id):
        if cam_id in self.active_cameras:
            self.active_cameras.remove(cam_id)
            print(f'Deactivated Camera {cam_id}.')
        else:
            print(f'Camera {cam_id} is not active.')

    def display_active_camera_feeds(self):
        if not self.active_cameras:
            print('No active cameras. Check the camera system.')
            return
        for cam_id in self.active_cameras:
            print(f'Feed from Camera {cam_id}: {self.camera_feed[cam_id - 1]}')

# Example usage
if __name__ == '__main__':
    camera_system = CameraSystem(camera_count=5)
    camera_system.activate_camera(1)
    camera_system.activate_camera(2)
    camera_system.display_active_camera_feeds()