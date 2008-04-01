%define	tmpwatch_cleaner	rpmrepackage
Summary:	Configuration for deleting old RPM repackage files
Summary(pl.UTF-8):	Konfiguracja tmpwatch czyszcząca stare pliki RPM repackage
Name:		tmpwatch-%{tmpwatch_cleaner}
Version:	0.1
Release:	0.9
License:	GPL v2
Group:		Applications/System
Source0:	%{name}.conf
Requires:	tmpwatch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Configuration for deleting old RPM repackage files.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/tmpwatch
cp -a %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/tmpwatch/%{tmpwatch_cleaner}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tmpwatch/%{tmpwatch_cleaner}.conf
