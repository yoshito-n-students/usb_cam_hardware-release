Name:           ros-melodic-usb-cam-controllers
Version:        0.0.4
Release:        0%{?dist}
Summary:        ROS usb_cam_controllers package

Group:          Development/Libraries
License:        TODO
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-camera-info-manager
Requires:       ros-melodic-controller-interface
Requires:       ros-melodic-controller-manager
Requires:       ros-melodic-cv-bridge
Requires:       ros-melodic-image-transport
Requires:       ros-melodic-pluginlib
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-usb-cam-hardware-interface
BuildRequires:  ros-melodic-camera-info-manager
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-controller-interface
BuildRequires:  ros-melodic-controller-manager
BuildRequires:  ros-melodic-cv-bridge
BuildRequires:  ros-melodic-image-transport
BuildRequires:  ros-melodic-pluginlib
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-usb-cam-hardware-interface

%description
The usb_cam_controllers package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Mon Mar 25 2019 yoshito <yoshito@todo.todo> - 0.0.4-0
- Autogenerated by Bloom

* Mon Mar 25 2019 yoshito <yoshito@todo.todo> - 0.0.3-0
- Autogenerated by Bloom

