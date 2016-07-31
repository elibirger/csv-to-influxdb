Summary: csv-to-influxdb
Name: csv-to-influxdb
Version: 0.1
Release: 1
License: GPL
Group: Essentials-il
BuildRoot: %{_tmppath}/%{name}-root
Source0: csv-to-influxdb-%{version}.tar.gz

%description
csv-to-influxdb by Essentials-il.

%prep
%setup 

%build

%install
cp csv-to-influxdb %{buildroot}/usr/bin

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(755,root,root)
/usr/bin/csv-to-influxdb

%changelog
*Thu  Jul 28 2016 Eli Birger
- Uberscript!
