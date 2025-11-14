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
  const [refreshing, setRefreshing] = useState(false);

  const fetchData = async () => {

    let url: string | null = 'https://cs-webapps.bu.edu/clchen5/dadjokes/api/jokes';
    const allJokes: Joke[] = [];

    while (url) {
      const response: Response = await fetch(url);
      const data = await response.json();

      console.log('API page data:', data);
      allJokes.push(...data.results); //ensures all jokes are shown and none hide due to pagination

      url = data.next; 
    }
    setJokes(allJokes)
  }

  const handleRefresh = () => {
    setRefreshing(true)
    fetchData()
    setRefreshing(false)
  }

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Jokes List</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />

       <FlatList data={jokes} renderItem={({ item }) => {
          return (
            <View>
              <Text >{item.text}</Text>
              <Text >{item.name}</Text>
            </View>
          )
        }} 

        ItemSeparatorComponent={() => (
          <View style={{height: 16, }} />
        )}
        ListEmptyComponent={<Text>No Jokes Found</Text>}
        ListHeaderComponent={<Text >Joke List</Text>}
        ListFooterComponent={<Text >End of list</Text>}
        refreshing={refreshing}
        onRefresh={handleRefresh}
        />
    
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
