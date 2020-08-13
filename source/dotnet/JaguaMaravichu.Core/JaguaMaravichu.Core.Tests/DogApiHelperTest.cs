using System;
using Xunit;

namespace JaguaMaravichu.Core.Tests
{
    public class DogApiHelperTest
    {
        [Fact]
        public void Breed_BreedId_SetsBreedName()
        {
            // Arrange
            Breed breed;

            // Act
            breed = new Breed("breedname-subbreedname");

            // Assert
            Assert.Equal("Breedname Subbreedname", breed.Name);
        }
    }
}