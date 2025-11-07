import { View, Text, Image, ImageBackground, ScrollView, Button, Pressable, Modal } from 'react-native'
import { useState } from "react";
const logoImg = require("./assets/adaptive-icon.png");

export default function App() {
  const [isModalVisible, setIsModalVisible] = useState(false)
  return (
   
  <View style={{ flex: 1, backgroundColor: "plum", padding : 60}}>  
   <Button title="Press" onPress={() => setIsModalVisible(true)} color="midnightblue"/>
   <Modal visible={isModalVisible} onRequestClose={() => setIsModalVisible(false)} animationType="slide"
    presentationStyle="pageSheet">
    <View style={{ flex: 1, backgroundColor: "lightblue", padding : 60}}>  
      <Text>Modal content</Text>
      <Button title="Close" color="midnightblue" onPress={() => setIsModalVisible(false)}/>
    </View>
   </Modal>

<ScrollView>
    <Button title="Press" onPress={() => console.log("Button pressed")} color="midnightblue" disabled/>
  <Text>
    <Text style={{ color: "white" }}>Hello</Text> World
  </Text> 
  {/* logoImg react can assume dimensions. for outside images, must specifiy dimensions */}
  <Pressable onPress={() => console.log("Image pressed")}>
    <Image source={logoImg} style={{ width: 300, height: 300 }} />
  </Pressable>
  <Pressable onPress={() => console.log("Text pressed")}>
    <Text>
      lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds. lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.
      lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.
      lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.lots of textsdfskljasdkjdsjsdksfkdsjfsdjfn dfhdsjflkjsdf df dfdf safsd sfdf fds fds sdfsdf asfds dsfas dsfdfds.
    </Text>
  </Pressable>
  <Image source={{ uri: "https://picsum.photos/300"}} style={{ width: 300, height: 300 }} /> 
    {/* <ImageBackground source={logoImg} style={{ flex: 1}}>
      <Text>IMAGE TEXT</Text>
    </ImageBackground>

    {/* <View style={{ width: 200, height: 200, backgroundColor: "lightblue"}}></View>
    <View style={{ width: 200, height: 200, backgroundColor: "lightgreen"}}></View> */}
   </ScrollView>
   
   </View> 
  
  ); 
}
