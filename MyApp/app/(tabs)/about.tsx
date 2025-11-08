// File: MyApp/app/(tabs)/about.tsx
// Author: Clarissa Chen (clchen5@bu.edu), 11/7/2025
// Description: Displays the about page

import { Text, View } from '@/components/Themed';
import { styles } from '../../assets/my_styles';
import { Image} from 'react-native';

export default function AboutScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>About</Text>
      <Text style={styles.subText}>Clarissa has lived in many cities in the past two years. She is in her travel era. She enjoys visiting friends, exploring, and eating delicious local food. </Text>

       
      <Image source={{ uri: "https://cs-people.bu.edu/clchen5/chicago.jpeg"}} style={{ width: 300, height: 300 }} /> 
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
    </View>
  );
}