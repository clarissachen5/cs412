import { StyleSheet, ActivityIndicator, TextInput, Button } from 'react-native';

import EditScreenInfo from '@/components/EditScreenInfo';
import { Text, View } from '@/components/Themed';
import { useState, useEffect } from "react";

export default function AddJokeScreen() {

    const [jokeText, setJokeText] = useState("")
    const [jokeName, setJokeName] = useState("")
    const [isLoading, setIsLoading] = useState(true)
    const [isPosting, setIsPosting] = useState(false)
    const [error, setError] = useState("")
    

    const addJoke = async () => {
        console.log("Submit pressed with:", { jokeText, jokeName });
        setIsPosting(true)
        try {
            const response = await fetch("https://cs-webapps.bu.edu/clchen5/dadjokes/api/jokes", {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    text: jokeText,
                    name: jokeName
                })
            })
            const newJoke = await response.json();
            console.log("response status", response.status)
            console.log("newJoke", newJoke)

            if (!response.ok) {
                console.log("Server rejected POST");
                setError("Failed to add new joke");
                return;
            }
            setJokeText("");
            setJokeName("");
            setIsPosting(false);
            setError("");
        } catch (error) {
            console.error("Error adding new joke", error)
            setError("Failed to add new joke")
        }

    }
    
    // if (isLoading) {
    //     return(
    //       <View>
    //         <ActivityIndicator size="large" color="0000ff" />
    //         <Text>Loading...</Text>
    //       </View>
    //     )
    //   }
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Add Joke</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />

      <TextInput placeholder="Joke Text" value={jokeText} onChangeText={setJokeText} />
      <TextInput placeholder="Joke Contributor Name" value={jokeName} onChangeText={setJokeName} />
      <Button title={isPosting ? "Adding...": "Add Joke"}
      onPress={addJoke}
      disabled={isPosting}/>


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
