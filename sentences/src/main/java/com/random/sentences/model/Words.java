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
            "accept","achieve","act","add","adjust","admire","allow","answer","appear","arrive",
            "ask","attack","build","break","bring","buy","call","carry","catch","change",
            "choose","clean","climb","close","collect","create","cut","decide","deliver","discover",
            "drive","eat","enter","escape","explore","fight","find","finish","fix","follow",
            "gain","give","grow","handle","help","hold","improve","jump","keep","know",
            "lead","learn","leave","listen","look","make","move","notice","open","organize",
            "paint","play","protect","push","reach","read","repair","run","save","search",
            "see","send","share","shoot","show","solve","speak","start","stop","study",
            "succeed","take","teach","tell","think","throw","travel","try","turn","understand",
            "use","wait","walk","watch","win","work","write","exploit","navigate","deploy"
        ));

        return verbs;
    }
}
