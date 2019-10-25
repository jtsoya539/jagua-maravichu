using System;
using System.Collections.Generic;

namespace JaguaMaravichuCore
{
    class QuizQuestion
    {
        public DogImage Image { get; set; }
        public List<Breed> Options { get; set; }
        private static Random random = new Random();
        private static DogApiHelper dogApiHelper = new DogApiHelper();

        public QuizQuestion(DogImage dogImage, int optionsNumber)
        {
            Image = dogImage;

            List<Breed> options = new List<Breed>();
            options.Add(dogImage.Breed);
            for (int i = 0; i < optionsNumber; i++)
            {
                int index = random.Next(DogApiHelper.Breeds.Count);
                options.Add(DogApiHelper.Breeds[index]);
            }

            Options = options;
        }
    }
}