import { Text, View} from '@/components/Themed';
import { styles } from '../../assets/my_styles';
import { ScrollView, Image} from 'react-native';

export default function DetailScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Cities Visited</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />


      <ScrollView>

           <Text style={styles.citiesText}>London</Text>
           <Image source={{ uri: "https://cs-people.bu.edu/clchen5/london.jpeg"}} style={{ width: 300, height: 300 }} /> 

           <Text style={styles.citiesText}>San Francisco</Text>
           <Image source={{ uri: "https://cs-people.bu.edu/clchen5/sanfrancisco.jpeg"}} style={{ width: 300, height: 300 }} /> 

           <Text style={styles.citiesText}>Boston</Text>
           <Image source={{ uri: "https://cs-people.bu.edu/clchen5/boston.jpeg"}} style={{ width: 300, height: 300 }} /> 

           <Text style={styles.citiesText}>Chicago</Text>
           <Image source={{ uri: "https://cs-people.bu.edu/clchen5/chicago.jpeg"}} style={{ width: 300, height: 300 }} /> 

          
      </ScrollView>
         
    </View>
  );
}
