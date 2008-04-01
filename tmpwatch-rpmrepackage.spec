Summary(pl.UTF-8):	Konfiguracja tmpwatch czyszcząca stare pliki rpm repackage
%define	tmpwatch_cleaner	rpmrepackage
Name:		tmpwatch-%{tmpwatch_cleaner}
Version:	0.1
Release:	0.9
License:	GPL v2
Group:		Applications/System
Source0:	%{name}.conf
# Source0-md5:	4fdcefdb36bc6c8ef5fea26eb4f1a2e3
Requires:	tmpwatch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -T -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/tmpwatch

install %SOURCE0 $RPM_BUILD_ROOT/etc/tmpwatch/%{tmpwatch_cleaner}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/tmpwatch/%{tmpwatch_cleaner}.conf
