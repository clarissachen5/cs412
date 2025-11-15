// File: DadJokes/app/(tabs)/jokes_list.tsx
// Author: Clarissa Chen (clchen5@bu.edu), 11/14/2025
// Description: Displays the jokes_list page

import { StyleSheet, FlatList, ActivityIndicator } from 'react-native';

import EditScreenInfo from '@/components/EditScreenInfo';
import { Text, View } from '@/components/Themed';
import { useState, useEffect } from "react";
import { styles } from '../../assets/my_styles';

export default function JokesListScreen() {

  type Joke = {
  text: string;
  name: string;
  }
  const [jokes, setJokes] = useState<Joke[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [error, setError] = useState("")
  const fetchData = async () => {
    try {

      let url: string | null = 'https://cs-webapps.bu.edu/clchen5/dadjokes/api/jokes';
      const allJokes: Joke[] = [];

      while (url) {
        const response: Response = await fetch(url);
        const data = await response.json();
        setIsLoading(false);
        console.log('API page data:', data);
        allJokes.push(...data.results); //ensures all jokes are shown and none hide due to pagination

        url = data.next; 
      }
      setJokes(allJokes)
    } catch (error) {
      console.error("Error fetching data:", error);
      setIsLoading(false);
      setError("Failed to fetch joke list")
    
    }
  }

  const handleRefresh = () => {
    setRefreshing(true)
    fetchData()
    setRefreshing(false)
  }

  useEffect(() => {
    fetchData();
  }, []);

  if (isLoading) {
        return(
          <View style={styles.loadingContainer}>
            <ActivityIndicator size="large" color="0000ff" />
            <Text>Loading...</Text>
          </View>
        )
      }
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Jokes List</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />

      {error ? (
        <View style={styles.errorContainer}>
          <Text style={styles.errorText}>{error}</Text>
        </View>
      ) : (<>
       <View style={styles.listContainer}>
        <FlatList data={jokes} renderItem={({ item }) => {
            return (
              <View style={styles.card}>
                <Text style={styles.titleText}>{item.text}</Text>
                <Text style={styles.bodyText}>{item.name}</Text>
              </View>
            )
          }} 

          ItemSeparatorComponent={() => (
            <View style={{height: 16, }} />
          )}
          ListEmptyComponent={<Text>No Jokes Found</Text>}
          ListHeaderComponent={<Text style={styles.bodyText}>Joke List</Text>}
          ListFooterComponent={<Text style={styles.bodyText}>End of list</Text>}
          refreshing={refreshing}
          onRefresh={handleRefresh}
          />
        </View>
        </> )}
    
    </View>

    
  );
}

