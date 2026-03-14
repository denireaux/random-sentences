package com.random.sentences.model;

import java.util.List;
import java.util.Random;

public class RandomSentence {

    public static String generateRandomSentence() {

        // Every sentence will go ->
            // [The] -> adj -> noun -> verb -> [The] -> adj -> noun
                // adj x2
                // noun x2
                // verb x1

        // Two adjectives...
        List<String> adjs = Words.adjectivesList();
        Random random = new Random();
        String adjective1 = adjs.get(random.nextInt(adjs.size()));
        String adjective2 = adjs.get(random.nextInt(adjs.size()));

        // Two nouns...
        List<String> nouns = Words.nounsList();
        String noun1 = nouns.get(random.nextInt(nouns.size()));
        String noun2 = nouns.get(random.nextInt(nouns.size()));

        // One verb...
        List<String> verbs = Words.verbsList();
        String verb = verbs.get(random.nextInt(verbs.size()));

        StringBuilder sentence = new StringBuilder();

        sentence.append("The ")
        .append(adjective1).append(" ")
        .append(noun1).append(" ")
        .append(verb).append(" ")
        .append("the ")
        .append(adjective2).append(" ")
        .append(noun2)
        .append(".");
        
        String result = sentence.toString();
        
        return result;
    }

    public static void main(String[] args) {
        String testRandomSentence = generateRandomSentence();
        System.out.println(testRandomSentence);
    }
    
}
