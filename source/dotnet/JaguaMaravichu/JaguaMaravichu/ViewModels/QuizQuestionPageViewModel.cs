using Acr.UserDialogs;
using JaguaMaravichu.Core;
using Prism.Commands;
using Prism.Mvvm;
using Prism.Navigation;
using System;
using System.Collections.Generic;
using System.Linq;

namespace JaguaMaravichu.ViewModels
{
    public class QuizQuestionPageViewModel : ViewModelBase
    {
        public QuizQuestionPageViewModel(INavigationService navigationService) : base(navigationService)
        {
        }

        private DogImage dogImage;
        public DogImage DogImage
        {
            get { return dogImage; }
            set { SetProperty(ref dogImage, value); }
        }

        public override async void Initialize(INavigationParameters parameters)
        {
            UserDialogs.Instance.ShowLoading("Loading...");
            DogImage = await DogApiHelper.GetRandomImageAsync();
            UserDialogs.Instance.HideLoading();
        }

        private DelegateCommand _refreshCommand;
        public DelegateCommand RefreshCommand =>
            _refreshCommand ?? (_refreshCommand = new DelegateCommand(ExecuteRefreshCommand, CanExecuteRefreshCommand));

        async void ExecuteRefreshCommand()
        {
            UserDialogs.Instance.ShowLoading("Loading...");
            DogImage = await DogApiHelper.GetRandomImageAsync();
            UserDialogs.Instance.HideLoading();
        }

        bool CanExecuteRefreshCommand()
        {
            return true;
        }
    }
}
