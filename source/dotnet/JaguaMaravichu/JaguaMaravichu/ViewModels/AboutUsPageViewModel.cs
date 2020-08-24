using Prism.Commands;
using Prism.Mvvm;
using Prism.Navigation;
using System;
using System.Collections.Generic;
using System.Linq;
using Xamarin.Essentials.Interfaces;

namespace JaguaMaravichu.ViewModels
{
    public class AboutUsPageViewModel : ViewModelBase
    {
        private readonly IAppInfo _appInfo;

        public AboutUsPageViewModel(INavigationService navigationService, IAppInfo appInfo)
            : base(navigationService)
        {
            _appInfo = appInfo;
            Title = "About Us";
            Version = _appInfo.VersionString;
        }

        private string _Version;
        public string Version
        {
            get { return _Version; }
            set { SetProperty(ref _Version, value); }
        }
    }
}
