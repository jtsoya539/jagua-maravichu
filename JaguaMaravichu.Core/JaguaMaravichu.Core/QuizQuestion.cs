using System;
using System.Collections.Generic;

namespace JaguaMaravichu.Core
{
    public class QuizQuestion
    {
        public DogImage Image { get; set; }
        public List<Breed> Options { get; set; }
        private static Random random = new Random();
        private static DogApiHelper dogApiHelper = new DogApiHelper();

        public QuizQuestion(DogImage dogImage, int optionsNumber)
        {
            Image = dogImage;
            Options = LoadOptions(dogImage.Breed, optionsNumber);
        }

        private List<Breed> LoadOptions(Breed answer, int optionsNumber)
        {
            List<Breed> options = new List<Breed>();
            int randomIndex;
            options.Add(answer);
            for (int i = 0; i < (optionsNumber - 1); i++)
            {
                do
                {
                    randomIndex = random.Next(DogApiHelper.Breeds.Count);
                } while (options.Contains(DogApiHelper.Breeds[randomIndex]));
                options.Add(DogApiHelper.Breeds[randomIndex]);
            }
            return options;
        }
    }
}