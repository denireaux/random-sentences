package com.random.sentences.model;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Words {
    public static List<String> adjectivesList() {
        List<String> adjectives = new ArrayList<>(Arrays.asList(
            "ancient","angry","bright","brave","calm","careful","clever","cold","cool","crazy",
            "dark","daring","delicate","eager","early","fancy","fast","fearless","fierce","gentle",
            "giant","glorious","graceful","happy","harsh","heavy","honest","hot","huge","icy",
            "jolly","kind","large","lazy","light","lively","lonely","loud","lucky","mighty",
            "modern","mysterious","narrow","neat","nervous","nice","noisy","odd","old","patient",
            "perfect","playful","polite","powerful","proud","quick","quiet","rare","rapid","rough",
            "royal","rusty","sad","safe","shiny","sharp","short","silent","simple","slow",
            "small","smart","smooth","soft","solid","strong","strange","sweet","swift","tall",
            "tender","thick","thin","tiny","tough","tricky","ugly","vast","warm","weak",
            "wild","wise","young","zealous","fragile","glowing","stormy","vivid","curious","bold"
        ));

        return adjectives;
    }

    public static List<String> nounsList() {
        List<String> nouns = new ArrayList<>(Arrays.asList(
            "apple","army","artist","beach","bird","blade","book","bridge","brother","castle",
            "cat","city","cloud","computer","crowd","desert","dream","engine","enemy","family",
            "fire","flower","forest","friend","game","garden","ghost","giant","girl","glass",
            "gold","group","heart","hero","hill","home","horse","house","idea","island",
            "jewel","journey","king","lake","leader","letter","machine","market","memory","mountain",
            "music","night","ocean","order","path","people","planet","power","queen","river",
            "road","rock","room","school","science","sea","shadow","ship","sky","soldier",
            "star","stone","storm","story","street","sun","system","teacher","team","tower",
            "tree","truth","valley","village","voice","war","water","weapon","wind","window",
            "world","writer","youth","zone","signal","device","network","mission","station","portal"
        ));

        return nouns;
    }

    public static List<String> verbsList() {
        List<String> verbs = new ArrayList<>(Arrays.asList(
            "accepted","achieved","acted","added","adjusted","admired","allowed","answered","appeared","arrived",
            "asked","attacked","built","broke","brought","bought","called","carried","caught","changed",
            "chose","cleaned","climbed","closed","collected","created","cut","decided","delivered","discovered",
            "drove","ate","entered","escaped","explored","fought","found","finished","fixed","followed",
            "gained","gave","grew","handled","helped","held","improved","jumped","kept","knew",
            "led","learned","left","listened","looked","made","moved","noticed","opened","organized",
            "painted","played","protected","pushed","reached","read","repaired","ran","saved","searched",
            "saw","sent","shared","shot","showed","solved","spoke","started","stopped","studied",
            "succeeded","took","taught","told","thought","threw","traveled","tried","turned","understood",
            "used","waited","walked","watched","won","worked","wrote","exploited","navigated","deployed"
        ));

        return verbs;
    }
}
