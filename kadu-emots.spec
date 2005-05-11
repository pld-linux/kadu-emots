# TODO
# - check License, Group
# - it shouldn't be only package for kadu

Summary:	Kadu - additional emots
Summary(pl):	Kadu - dodatkowe emotikonki
Name:		kadu-emots
Version:	01
Release:	1
License:	Artistic
Group:		Applications/Communications
Source0:	http://www.kadu.net/download/additions/%{name}-zestaw288.tar.bz2
# Source0-md5:	98a378047ea252f7277e978f06f9a6bb
Requires:	kadu
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kadu - additional emots.

%description -l pl
Kadu - dodatkowe emotikonki.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/kadu/themes/emoticons/gadu-gadu/{3,4,5,6,7,8,9}
for i in `seq 3 9`
do
  install zestaw_288/$i/{*.gif,emots.txt} $RPM_BUILD_ROOT%{_datadir}/kadu/themes/emoticons/gadu-gadu/$i
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/kadu/themes/emoticons/gadu-gadu/
