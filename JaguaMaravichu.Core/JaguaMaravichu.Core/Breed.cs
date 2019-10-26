using System;
using System.Globalization;

namespace JaguaMaravichu.Core
{
    class Breed
    {
        public string Id { get; set; }
        public string Name { get; set; }

        public Breed(string id)
        {
            Id = id;
            TextInfo ti = CultureInfo.CurrentCulture.TextInfo;
            Name = ti.ToTitleCase(id.Replace('-', ' '));
        }
    }
}