using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace JaguaMaravichuCore
{
    class DogApiHelper
    {
        public static List<Breed> Breeds { get; set; }
        private static readonly HttpClient client = new HttpClient();

        private static DogImage ParseRandomImage(string json)
        {
            DogImage result;
            JObject dogApiResponse = JObject.Parse(json);
            string message = dogApiResponse["message"].ToString();

            Uri dogImageUrl = new Uri(message);

            result = new DogImage
            {
                Url = message,
                Breed = new Breed(dogImageUrl.Segments[2].Replace("/", ""))
            };

            return result;
        }


        private static List<Breed> ParseBreedsList(string json)
        {
            List<Breed> result = new List<Breed>();

            JObject dogApiResponse = JObject.Parse(json);
            string message = dogApiResponse["message"].ToString();

            Dictionary<string, List<string>> breeds = JsonConvert.DeserializeObject<Dictionary<string, List<string>>>(message);

            foreach (KeyValuePair<string, List<string>> pair in breeds)
            {
                if (pair.Value.Count == 0)
                {
                    result.Add(new Breed(pair.Key));
                }
                else
                {
                    foreach (var subbreed in pair.Value)
                    {
                        result.Add(new Breed(pair.Key + "-" + subbreed));
                    }
                }
            }

            return result;
        }

        public static async Task<DogImage> GetRandomImageAsync()
        {
            var jsonTask = await client.GetStringAsync("https://dog.ceo/api/breeds/image/random");
            return ParseRandomImage(jsonTask);
        }

        public static async Task<List<Breed>> GetBreedsAsync()
        {
            var jsonTask = await client.GetStringAsync("https://dog.ceo/api/breeds/list/all");
            return ParseBreedsList(jsonTask);
        }

    }
}