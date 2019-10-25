using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

namespace JaguaMaravichuCore
{
    class Program
    {
        private static readonly DogApiHelper dogApiHelper = new DogApiHelper();

        static void Main(string[] args)
        {
            DogApiHelper.Breeds = DogApiHelper.GetBreedsAsync().Result;
            DogImage dogImage = DogApiHelper.GetRandomImageAsync().Result;
            QuizQuestion quizQuestion = new QuizQuestion(dogImage, 3);

            foreach (var item in DogApiHelper.Breeds)
            {
                Console.WriteLine(item.Id + "  /  " + item.Name);
            }

            Console.WriteLine("--------------------------");

            Console.WriteLine($"Url: {quizQuestion.Image.Url}");
            Console.WriteLine($"Breed.Id: {quizQuestion.Image.Breed.Id}");
            Console.WriteLine($"Breed.Name: {quizQuestion.Image.Breed.Name}");

            Console.WriteLine("--------------------------");

            foreach (var item in quizQuestion.Options)
            {
                Console.WriteLine(item.Id + "  /  " + item.Name);
            }

            //ProcessBreedsList().Wait();
            //ProcessRandomImage().Wait();
        }

/*
        private static async Task ProcessBreedsList()
        {
            client.DefaultRequestHeaders.Accept.Clear();

            var stringTask = client.GetStringAsync("https://dog.ceo/api/breeds/list/all");

            var msg = await stringTask;
        }

        private static async Task ProcessRandomImage()
        {
            client.DefaultRequestHeaders.Accept.Clear();

            var stringTask = client.GetStringAsync("https://dog.ceo/api/breeds/image/random");

            var msg = await stringTask;
        }
 */

    }
}
