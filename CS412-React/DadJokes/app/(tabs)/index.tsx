import { StyleSheet, FlatList, Image } from 'react-native';

import EditScreenInfo from '@/components/EditScreenInfo';
import { Text, View } from '@/components/Themed';
import { useState, useEffect } from "react";

export default function IndexScreen() {
  const [joke, setJoke] = useState("")
  const [picture, setPicture] = useState("")
  const [isLoading, setIsLoading] = useState(true)
  const [contributor, setContributor] = useState("")
  const fetchData = async () => {
    const jokeResponse = await fetch(
      `http://127.0.0.1:8000/dadjokes/api/random`
    );
    const jokeData = await jokeResponse.json()
    setJoke(jokeData.text)
    setContributor(jokeData.name)

    const pictureResponse = await fetch(
      `http://127.0.0.1:8000/dadjokes/api/random_picture`
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
      
      
      <View>
          <Text>{joke}</Text>
          <Text>{contributor}</Text>
          <Image source={{ uri: picture }} style={{ width: 300, height: 300 }} /> 

      </View>
         
      
      
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
});
