%define install_prefix /opt/task
%define __os_install_post %{nil}

Name:		test-task
Version:	0.1
Release:	1%{?dist}
Summary:	Test task packaged app
License:    Free
Prefix: %{install_prefix}
Source:	test-task.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
AutoReqProv: no

Requires:   python
Requires:   python-pip

BuildArch:  noarch

%description
Test task packaged app

%prep
%setup -n src


%install
mkdir -p $RPM_BUILD_ROOT%{install_prefix}
for i in application.py settings.py manager.py requirements.txt
do
  cp $i $RPM_BUILD_ROOT%{install_prefix}
done

%clean
rm -rf %{buildroot}


%files
%defattr(644,root,root,-)
%{install_prefix}/application.py
%{install_prefix}/requirements.txt
%attr(755,root,root) %{install_prefix}/manager.py
%config %{install_prefix}/settings.py


%changelog

* Fri Sep 20 2015 CCS BDaaS <galanoff@gmail.com> - 0.1
- Release 0.1
