%define         datapath %{_datadir}/smc/

Name:           smc-music
Version:        4.0
Release:        3%{?dist}
Summary:        Additional music for Secret Maryo Chronicles
Group:          Amusements/Games
License:        GPLv3
URL:            http://www.secretmaryo.org
Source0:        http://dl.sf.net/smclone/SMC_music_%{version}_high.zip
Source1:        dochelper.pl
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       smc >= 0.99.7

%description
Additional music for the game Secret Maryo Chronicles


%prep
%setup -qc
#Fix EOL chars
sed -i 's/\r//' docs/license.txt


%build
# Generate the credit list from lots of little text files scattered around the
# installation. Very messy! A helper script is used to avoid over-complicating
# the spec. Additional processing is done on the credits to strip 'data/' from
# the paths because the installation location is now different and it's far
# simpler that altering dochelper.pl
cp %{SOURCE1} . && perl dochelper.pl
sed -i 's/\r//' credits.txt
sed -i 's|data/||g' credits.txt


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{datapath}/music/{game,land,overworld,story}
install -pm0644 data/music/game/*.ogg %{buildroot}%{datapath}/music/game
install -pm0644 data/music/land/*.ogg %{buildroot}%{datapath}/music/land
install -pm0644 data/music/overworld/*.ogg %{buildroot}%{datapath}/music/overworld
install -pm0644 data/music/story/*.ogg %{buildroot}%{datapath}/music/story

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc credits.txt docs/license.txt
%{datapath}/music/*


%changelog
* Wed Dec 17 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 4.0-3
- Fix directory ownership issues (rpmfusion 223)

* Fri Jul 25 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 4.0-2
- Release bump for rpmfusion

* Wed Aug 08 2007 Ian Chapman <packages@amiga-hardware.com> 4.0-1
- Upgrade to 4.0
- Changed license field due to match new guidelines

* Sat Jun 02 2007 Ian Chapman <packages@amiga-hardware.com> 3.1-2
- Minor changes due to new data location in smc

* Fri Oct 06 2006 Ian Chapman <packages@amiga-hardware.com> 3.1-1
- Upgrade to 3.1

* Sun Jul 09 2006 Ian Chapman <packages@amiga-hardware.com> 3.0-2
- Corrected EOL chars in credits.txt
- Removed redundant params from %%setup

* Sun Jun 25 2006 Ian Chapman <packages@amiga-hardware.com> 3.0-1
- Initial Release