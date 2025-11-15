// File: DadJokes/app/(tabs)/index.tsx
// Author: Clarissa Chen (clchen5@bu.edu), 11/14/2025
// Description: Displays the index page
import { StyleSheet, FlatList, Image } from 'react-native';

import EditScreenInfo from '@/components/EditScreenInfo';
import { Text, View } from '@/components/Themed';
import { useState, useEffect } from "react";
import { styles } from '../../assets/my_styles';

export default function IndexScreen() {
  const [joke, setJoke] = useState("")
  const [picture, setPicture] = useState("")
  const [isLoading, setIsLoading] = useState(true)
  const [contributor, setContributor] = useState("")
  const [error, setError] = useState("")
  const fetchData = async () => {
    const jokeResponse = await fetch(
      `https://cs-webapps.bu.edu/clchen5/dadjokes/api/random`
    );
    const jokeData = await jokeResponse.json()
    setJoke(jokeData.text)
    setContributor(jokeData.name)

    const pictureResponse = await fetch(
      `https://cs-webapps.bu.edu/clchen5/dadjokes/api/random_picture`
    );
    const pictureData = await pictureResponse.json()
    setPicture(pictureData.image_url)
    setIsLoading(false);

  }

  useEffect(() => {
      fetchData();
    }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Index</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      
      {error ? (
        <View style={styles.errorContainer}>
          <Text style={styles.errorText}>{error}</Text>
        </View>
      ) : (<>
      <View style={styles.card}>
          <Text style={styles.titleText}>Joke: {joke}</Text>
          <Text style={styles.bodyText}>By: {contributor}</Text>
          <Image source={{ uri: picture }} style={{ width: 300, height: 300 }} /> 

      </View>
         
      </>)}
      
    </View>
  );
}

