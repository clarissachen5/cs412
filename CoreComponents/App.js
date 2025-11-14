import { View, StyleSheet, FlatList, Text, ActivityIndicator, TextInput, Image, ImageBackground, ScrollView, Button, Pressable, Modal, SafeAreaView, StatusBar } from 'react-native'
import { useState, useEffect } from "react";
const logoImg = require("./assets/adaptive-icon.png");

export default function App() {
  // const [isModalVisible, setIsModalVisible] = useState(false)

  const [postList, setPostList] = useState([])
  const [isLoading, setIsLoading] = useState(true)
  const [refreshing, setRefreshing] = useState(false)
  const [postTitle, setPostTitle] = useState("")
  const [postBody, setPostBody] = useState("")
  const [isPosting, setIsPosting] = useState(false)
  const [error, setError] = useState("")

  const fetchData= async (limit = 10) => {
    try {

    
    const response = await fetch(
      `https://jsonplaceholder.typicode.com/posts?_limit=${limit}`
    );
    const data = await response.json()
    setPostList(data)
    setIsLoading(false);
    setError("");
    } catch (error) {
      console.error("Error fetching data:", error);
      setIsLoading(false);
      setError("Failed to fetch post list")
    }
  };

  const handleRefresh = () => {
    setRefreshing(true)
    fetchData(20)
    setRefreshing(false)
  }

  const addPost = async () => {
    setIsPosting(true)
    try {

    
    const response = await fetch("https://jsonplaceholder.typicode.com/posts", {
      method: 'post',
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        title: postTitle,
        body: postBody
      })
    })
    const newPost = await response.json()
    setPostList([newPost, ...postList])
    setPostTitle("");
    setPostBody("");
    setIsPosting(false);
    setError("");
    } catch (error) {
      console.error("Error adding new post", error)
      setError("Failed to add new post")
    }
  }

  useEffect(() => {
    fetchData();
  }, []);

  if (isLoading) {
    return(
      <SafeAreaView style={styles.loadingContainer}>
        <ActivityIndicator size="large" color="0000ff" />
        <Text>Loading...</Text>
      </SafeAreaView>
    )
  }
  return (
    <SafeAreaView style={styles.container}>
      {error ? (
        <View style={styles.errorContainer}>
          <Text style={styles.errorText}>{error}</Text>
        </View>
      ) : (<>
      <View style={styles.inputContainer}>
        <TextInput style={styles.input} placeholder="Post title" value={postTitle} onChangeText={setPostTitle}/>
        <TextInput style={styles.input} placeholder="Post body" value={postBody} onChangeText={setPostBody}/>
        <Button title={isPosting ? "Adding..." : "Add Post"} 
        onPress={addPost} 
        disabled={isPosting}/>
      </View>
      <View style={styles.listContainer}>
        <FlatList data={postList} renderItem={({ item }) => {
          return (
            <View style={styles.card} >
              <Text style={styles.titleText}>{item.title}</Text>
              <Text style={styles.bodyText}>{item.body}</Text>
            </View>
          )
        }} 

        ItemSeparatorComponent={() => (
          <View style={{height: 16, }} />
        )}
        ListEmptyComponent={<Text>No Posts Found</Text>}
        ListHeaderComponent={<Text style={styles.headerText}>Post List</Text>}
        ListFooterComponent={<Text style={styles.footerText}>End of list</Text>}
        refreshing={refreshing}
        onRefresh={handleRefresh}
        />
      </View>
      </>)}
    </SafeAreaView>
   
//   <View style={{ flex: 1, backgroundColor: "plum", padding : 60}}>  
//    <Button title="Press" onPress={() => setIsModalVisible(true)} color="midnightblue"/>
//    <Modal visible={isModalVisible} onRequestClose={() => setIsModalVisible(false)} animationType="slide"
//     presentationStyle="pageSheet">
//     <View style={{ flex: 1, backgroundColor: "lightblue", padding : 60}}>  
//       <Text>Modal content</Text>
//       <Button title="Close" color="midnightblue" onPress={() => setIsModalVisible(false)}/>
//     </View>
//    </Modal>

// <ScrollView>
//     <Button title="Press" onPress={() => console.log("Button pressed")} color="midnightblue" disabled/>
//   <Text>
//     <Text style={{ color: "white" }}>Hello</Text> World
//   </Text> 
//   {/* logoImg react can assume dimensions. for outside images, must specifiy dimensions */}
//   <Pressable onPress={() => console.log("Image pressed")}>
//     <Image source={logoImg} style={{ width: 300, height: 300 }} />
//   </Pressable>
//   <Pressable onPress={() => console.log("Text pressed")}>
//     <Text>
//       lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds. lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.
//       lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.
//       lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.
//     </Text>
//   </Pressable>
//   <Image source={{ uri: "https://picsum.photos/300"}} style={{ width: 300, height: 300 }} /> 
    /* <ImageBackground source={logoImg} style={{ flex: 1}}>
      <Text>IMAGE TEXT</Text>
    </ImageBackground>

    {/* <View style={{ width: 200, height: 200, backgroundColor: "lightblue"}}></View>
    <View style={{ width: 200, height: 200, backgroundColor: "lightgreen"}}></View> */
  //  </ScrollView>
   
  //  </View> 
  
  ); 
}

const styles = StyleSheet.create({
  container: {
    flex: 1, 
    backgroundColor: '#f5f5f5',
    paddingTop: StatusBar.currentHeight
  },
  listContainer: {
    flex: 1,
    paddingHorizational: 16,
  },
  card: {
    backgroundColor: "white",
    padding: 16,
    borderRadius: 8,
    borderWidth: 1,
  },
  titleText: {
    fontSize: 30,
  },
  bodyText: {
    fontSize: 24,
    color: "#666666"
  },
  loadingContainer: {
    flex: 1,
    backgroundColor: "#F5F5F5",
    paddingTop: StatusBar.currentHeight,
    justifyContent: "center", 
    alignItems: "center",
  },
  inputContainer: {
    backgroundColor: "white",
    padding: 16,
    borderRadius: 8,
    borderWidth: 1,
    margin: 16,
  },
  input: {
    height: 40,
    borderColor: "gray",
    borderWidth: 1,
    marginBottom: 8,
    padding: 8,
    borderRadius: 8,
  },
  errorContainer: {
    backgroundColor: "#FFC0CB",
    padding: 16,
    borderRadius: 8,
    borderWidth: 1,
    margin: 16,
    alignItems: "center",
  },
  errorText: {
    color: "#D8000C",
    fontSize: 16, 
    textAlign: "center",
  }
});