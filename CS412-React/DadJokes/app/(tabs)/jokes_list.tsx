import { StyleSheet, FlatList } from 'react-native';

import EditScreenInfo from '@/components/EditScreenInfo';
import { Text, View } from '@/components/Themed';
import { useState, useEffect } from "react";


export default function JokesListScreen() {

  type Joke = {
  text: string;
  name: string;
  }
  const [jokes, setJokes] = useState<Joke[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  const fetchData = async () => {
    const response = await fetch(
       `http://127.0.0.1:8000/dadjokes/api/jokes`
    );
    const data = await response.json()
    console.log('API data:', data); 
    setJokes(data.results)
  }

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Jokes List</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
       

      {jokes.map((joke, index) => (
        <View key={index} style={{ marginBottom: 16 }}>
          <Text>{joke.text}</Text>
          <Text>{joke.name}</Text>
        </View>
      ))}
    
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
