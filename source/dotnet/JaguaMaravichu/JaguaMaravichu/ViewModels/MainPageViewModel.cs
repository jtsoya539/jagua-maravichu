using Prism.Commands;
using Prism.Mvvm;
using Prism.Navigation;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Xamarin.Essentials.Interfaces;

namespace JaguaMaravichu.ViewModels
{
    public class MainPageViewModel : ViewModelBase
    {
        private readonly IAppInfo _appInfo;

        public MainPageViewModel(INavigationService navigationService, IAppInfo appInfo)
            : base(navigationService)
        {
            _appInfo = appInfo;
            Title = "Jagua Maravichu";
            PackageName = _appInfo.PackageName;
        }

        private string packageName;
        public string PackageName
        {
            get { return packageName; }
            set { SetProperty(ref packageName, value); }
        }

        private DelegateCommand _PlayCommand;
        public DelegateCommand PlayCommand => _PlayCommand ?? (_PlayCommand = new DelegateCommand(ExecutePlayCommand, CanExecutePlayCommand));

        void ExecutePlayCommand()
        {
            NavigationService.NavigateAsync("/QuizQuestionPage");
        }

        bool CanExecutePlayCommand()
        {
            return true;
        }
    }
}
