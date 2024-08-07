%define         datapath %{_datadir}/smc/

Name:           smc-music
Version:        4.1
Release:        19%{?dist}
Summary:        Additional music for Secret Maryo Chronicles
Group:          Amusements/Games
License:        GPLv3
URL:            http://www.secretmaryo.org
Source0:        http://dl.sf.net/smclone/SMC_Music_%{version}_high.zip
Source1:        dochelper.pl
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl
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
* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Nov 01 2012 Nicolas Chauvet <kwizart@gmail.com> - 4.1-3
- Rebuilt for new boost

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Apr 15 2009 Hans de Goede <j.w.r.degoede@hhs.nl> 4.1-1
- New upstream release 4.1

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 4.0-4
- rebuild for new F11 features

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
