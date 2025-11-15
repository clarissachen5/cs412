// File: DadJokes/app/(tabs)/add_joke.tsx
// Author: Clarissa Chen (clchen5@bu.edu), 11/14/2025
// Description: Displays the add_joke page

import { StyleSheet, ActivityIndicator, TextInput, Button } from 'react-native';

import EditScreenInfo from '@/components/EditScreenInfo';
import { Text, View } from '@/components/Themed';
import { useState, useEffect } from "react";
import { styles } from '../../assets/my_styles';

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
    
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Add Joke</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />

        {error ? (
        <View style={styles.errorContainer}>
          <Text style={styles.errorText}>{error}</Text>
        </View>
      ) : (<>
       <View style={styles.inputContainer}>
        <TextInput style={styles.input} placeholder="Joke Text" value={jokeText} onChangeText={setJokeText} />
        <TextInput style={styles.input} placeholder="Joke Contributor Name" value={jokeName} onChangeText={setJokeName} />
        <Button title={isPosting ? "Adding...": "Add Joke"}
        onPress={addJoke}
        disabled={isPosting}/>
      </View>

        </>)}
    </View>
  );

}

