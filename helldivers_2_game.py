from __future__ import annotations
import random
from typing import List
import functools
from dataclasses import dataclass
from Options import OptionSet, Toggle
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class Helldivers2ArchipelagoOptions:
    helldivers_2_warbonds: warbonds
    helldivers_2_DLC: super_citizen
    helldivers_2_superstore_primary: superstore_primary
    helldivers_2_superstore_secondary: superstore_secondary
    helldivers_2_superstore_armors: superstore_armor

class Helldivers2Game(Game):
    name = "Helldivers 2"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = True

    options_cls = Helldivers2ArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Play on Super Helldive difficulty",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label="Play as a solo Helldiver",
                data=dict(),
            ),
        ]
    

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Complete a full 3 mission operation against the FACTION",
                data={
                    "FACTION": (self.factions, 1),
                    },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete a mission against the FACTION",
                data={
                    "FACTION": (self.factions, 1),
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Perform a full clear on a 40 minutes or blitz mision against the FACTION",
                data={
                    "FACTION": (self.factions, 1),
                    },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete a mission with the following equipment:  PRIMARY, SECONDARY, THROWABLE, ARMOR",
                data={
                    "PRIMARY": (self.primary_weapons, 1),
                    "SECONDARY": (self.secondary_weapons, 1),
                    "THROWABLE": (self.trowable, 1),
                    "ARMOR": (self.armor, 1)
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Complete a mission with the following stratagems: STRATAGEM, BOOSTER",
                data={
                    "STRATAGEM": (self.stratagems, 4),
                    "BOOSTER": (self.booster, 1)
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
        ]
        if self.include_super_citizens:
            templates.append(
                GameObjectiveTemplate(
                    label="Complete ROUNDS rounds on the stratagem hero minigame",
                    data= {
                        "ROUNDS": (self.rounds, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                )
            )
        return templates
    
    
    @property
    def include_super_citizens(self) -> bool:
        return bool(self.archipelago_options.helldivers_2_DLC.value)
    @property
    def warbonds_owned(self) -> List[str]:
        return sorted(self.archipelago_options.helldivers_2_warbonds.value)
    @property
    def has_helldivers_movilize(self) -> bool:
        return "Helldivers Movilize" in self.warbonds_owned
    @property
    def has_steeled_veterans(self) -> bool:
        return "Steeled Veterans" in self.warbonds_owned
    @property
    def has_cutting_edge(self) -> bool:
        return "Cutting Edge" in self.warbonds_owned
    @property
    def has_democratic_detonation(self) -> bool:
        return "Democratic Detonation" in self.warbonds_owned
    @property
    def has_polar_patriots(self) -> bool:
        return "Polar Patriots" in self.warbonds_owned
    @property
    def has_viper_commandos(self) -> bool:
        return "Viper Commandos" in self.warbonds_owned
    @property
    def has_freedoms_flame(self) -> bool:
        return "Freedom's Flame" in self.warbonds_owned
    @property
    def has_chemical_agents(self) -> bool:
        return "Chemical Agents" in self.warbonds_owned
    @property
    def has_truth_enforcers(self) -> bool:
        return "Truth Enforcers" in self.warbonds_owned
    @property
    def has_urban_legends(self) -> bool:
        return "Urban Legends" in self.warbonds_owned
    @property
    def has_servants_of_freedom(self) -> bool:
        return "Servants of Freedom" in self.warbonds_owned
    @property
    def has_borderline_justice(self) -> bool:
        return "Borderline Justice" in self.warbonds_owned
    @property
    def has_masters_of_ceremony(self) -> bool:
        return "Masters of Ceremony" in self.warbonds_owned
    @property
    def has_force_of_law(self) -> bool:
        return "Force of Law" in self.warbonds_owned
    @property
    def has_control_group(self) -> bool:
        return "Control Group" in self.warbonds_owned
    @property
    def has_halo_odst(self) -> bool:
        return "Halo ODST" in self.warbonds_owned
    
    
    @staticmethod
    def factions() -> List[str]:
        return [
            "Automatons",
            "Terminids",
            "Illuminates"
        ]
    
    @staticmethod
    def rounds() -> range:
        return range(5, 10)

    
    @functools.cached_property
    def primary_base(self) -> List[str]:
        return ["AR-23 Liberator",
                "R-2124 Constitution"
        ]
    
    @functools.cached_property
    def secondary_base(self) -> List[str]:
        return ["P-2 Peacemaker"]
    
    @functools.cached_property
    def trowable_base(self) -> List[str]:
        return ["G-12 High Explosive"]
    
    @functools.cached_property
    def stratagem_base(self) -> List[str]:
        stratagem = ["MG-43 Machine Gun",
                "APW-1 Anti-Materiel Rifle",
                "M-105 Stalwart",
                "EAT-17 Expendable Anti-Tank",
                "GR-8 Recoilless Rifle",
                "FLAM-40 Flamethrower",
                "AC-8 Autocannon",
                "MG-206 Heavy Machine Gun",
                "RL-77 Airburst Rocket Launcher",
                "MLS-4X Commando",
                "RS-422 Railgun",
                "FAF-14 Spear",
                "StA-X3 W.A.S.P. Launcher",
                "Orbital Gatling Barrage",
                "Orbital Airburst Strike",
                "Orbital 120mm HE Barrage",
                "Orbital 380mm HE Barrage",
                "Orbital Walking Barrage",
                "Orbital Laser",
                "Orbital Railcannon Strike",
                "Eagle Strafing Run",
                "Eagle Airstrike",
                "Eagle Cluster Bomb",
                "Eagle Napalm Airstrike",
                "LIFT-850 Jump Pack",
                "Eagle Smoke Strike",
                "Eagle 110mm Rocket Pods",
                "Eagle 500Kg Bomb",
                "M-102 Fast Recon Vehicle",
                "Orbital Precision Strike",
                "Orbital Gas Strike",
                "Orbital EMS Strike",
                "Orbital Smoke Strike",
                "E/MG-101 HMG Emplacement",
                "FX-12 Shield Generator Relay",
                "A/ARC-3 Tesla Tower",
                "E/GL-21 Grenadier Battlement",
                "MD-6 Anti-Personnel Minefield",
                "B-1 Supply Pack",
                "GL-21 Grenade Launcher",
                "LAS-98 Laser Cannon",
                "MD-I4 Incendiary Mines",
                'AX/LAS-5 "Guard Dog" Rover',
                "SH-20 Ballistic Shield Backpack",
                "ARC-3 Arc Thrower",
                "MD-17 Anti-Tank Mines",
                "LAS-99 Quasar Cannon",
                "SH-32 Shield Generator Pack",
                "MD-8 Gas Mines",
                "A/MG-43 Machine Gun Sentry",
                "A/G-16 Gatling Sentry",
                "A/M-12 Mortar Sentry",
                'AX/AR-23 "Guard Dog"',
                "A/AC-8 Autocannon Sentry",
                "A/MLS-4X Rocket Sentry",
                "A/M-23 EMS Mortar Sentry"
        ]
        mechs = [
            "EXO-45 Patriot Exosuit",
            "EXO-49 Emancipator Exosuit"
        ]
        random.shuffle(mechs)
        stratagem.append(mechs[0])
        return stratagem
    
    @functools.cached_property
    def armor_base(self) -> List[str]:
        return [
            "B-01 Tactical",
            "TR-117 Alpha Commander",
            "DP-00 Tactical"
        ]
    
    @functools.cached_property
    def super_citizen_primary(self) -> List[str]:
        return ["MP-98 Knight"]
    
    @functools.cached_property
    def super_citizen_armor(self) -> List[str]:
        return ["DP-53 Savior of the Free"]
    
    @functools.cached_property
    def helldivers_movilize_primary(self) -> List[str]:
        return [
            "SG-8 Punisher",
            "R-63 Dilience",
            "SMG-37 Defender",
            "SG-225 Breaker",
            "LAS-5 Scythe",
            "AR-23P Liberator Penetrator",
            "R-63CS Diligence Counter Sniper",
            "SG-8S Slugger",
            "SG-225SP Breaker Spray&Pray",
            "PLAS-1 Scorcher"
        ]
    
    @functools.cached_property
    def helldivers_movilize_secondary(self) -> List[str]:
        return [
            "P-19 Redeemer"
        ]
    
    @functools.cached_property
    def helldivers_movilize_trowable(self) -> List[str]:
        return [
            "G-6 Frag",
            "G-16 Impact",
            "G-3 Smoke"
        ]
    
    @functools.cached_property
    def helldivers_movilize_booster(self) -> List[str]:
        return [
            "Hellpod Space Optimization",
            "Vitality Enhancement",
            "UAV Recon Booster",
            "Stamina Enhancement",
            "Muscle Enhancement",
            "Increased Reinforcement Budget"
        ]
    
    @functools.cached_property
    def helldivers_movilize_armor(self) -> List[str]:
        return [
            "SC-34 Infiltrator",
            "FS-05 Marksman",
            "CE-35 Trench Engineer",
            "CM-09 Bonesnapper",
            "DP-40 Hero of the Federation",
            "FS-23 Battle Master",
            "SC-30 Trailblazer Scout",
            "SA-04 Combat Technician",
            "CM-14 Physician",
            "DP-11 Champion of the People"
        ]
    
    @functools.cached_property
    def steeled_veterans_primary(self) -> List[str]:
        return [
            "AR-23C Liberator Concussive",
            "SG-225IE Breaker Incendiary",
            "JAR-5 Dominator"
        ]
    
    @functools.cached_property
    def steeled_veterans_secondary(self) -> List[str]:
        return ["P-4 Senator"]
    
    @functools.cached_property
    def steeled_veterans_trowable(self) -> List[str]:
        return ["G-10 Incendiary"]
    
    @functools.cached_property
    def steeled_veterans_booster(self) -> List[str]:
        return ["Flexible Reinforcement Budget"]
    
    @functools.cached_property
    def steeled_veterans_armor(self) -> List[str]:
        return [
            "SA-25 Steel Trooper",
            "SA-12 Servo Assisted",
            "SA-32 Dynamo"
        ]
    
    @functools.cached_property
    def cutting_edge_primary(self) -> List[str]:
        return [
            "LAS-16 Sickle",
            "SG-8P Punisher Plasma",
            "ARC-12 Blitzer"
        ]
    
    @functools.cached_property
    def cutting_edge_secondary(self) -> List[str]:
        return ["LAS-7 Dagger"]
    
    @functools.cached_property
    def cutting_edge_trowable(self) -> List[str]:
        return ["G-23 Stun"]
    
    @functools.cached_property
    def cutting_edge_booster(self) -> List[str]:
        return ["Localization Confusion"]
    
    @functools.cached_property
    def cutting_edge_armor(self) -> List[str]:
        return [
            "EX-03 Prototype 3",
            "EX-16 Prototype 16",
            "EX-00 Prototype X"
        ]
    
    @functools.cached_property
    def democratic_detonation_primary(self) -> List[str]:
        return [
            "BR-14 Adjudicator",
            "R-36 Eruptor",
            "CB-9 Exploding Crossbow"
        ]
    
    @functools.cached_property
    def democratic_detonation_secondary(self) -> List[str]:
        return ["GP-31 Granade Pistol"]
    
    @functools.cached_property
    def democratic_detonation_trowable(self) -> List[str]:
        return ["G-123 Thermite"]
    
    @functools.cached_property
    def democratic_detonation_booster(self) -> List[str]:
        return ["Expert Extraction Pilot"]
    
    @functools.cached_property
    def democratic_detonation_armor(self) -> List[str]:
        return [
            "CE-27 Ground Breaker",
            "CE-07 Demolition Specialist",
            "FS-55 Devastator"
        ]
    
    @functools.cached_property
    def polar_patriots_primary(self) -> List[str]:
        return [
            "AR-61 Tenderizer",
            "SMG-72 Pummeler",
            "PLAS-101 Purifier"
        ]
    
    @functools.cached_property
    def polar_patriots_secondary(self) -> List[str]:
        return ["P-113 Veredict"]
    
    @functools.cached_property
    def polar_patriots_trowable(self) -> List[str]:
        return ["G-13 Incendiary Impact"]
    
    @functools.cached_property
    def polar_patriots_booster(self) -> List[str]:
        return ["Motivational Shocks"]
    
    @functools.cached_property
    def polar_patriots_armor(self) -> List[str]:
        return [
            "CW-36 Winter Warrior",
            "CW-22 Kodiak",
            "CW-4 Artic Ranger"
        ]
    
    @functools.cached_property
    def viper_commandos_primary(self) -> List[str]:
        return ["AR-23A Liberator Carbine"]
    
    @functools.cached_property
    def viper_commandos_secondary(self) -> List[str]:
        return ["SG-22 Bushwhacker"]
    
    @functools.cached_property
    def viper_commandos_trowable(self) -> List[str]:
        return ["K-2 Throwing Knife"]
    
    @functools.cached_property
    def viper_commandos_booster(self) -> List[str]:
        return ["Experimental Infusion"]
    
    @functools.cached_property
    def viper_commandos_armor(self) -> List[str]:
        return [
            "PH-9 Predator",
            "PH-202 Twigsnapper"
        ]
        
    @functools.cached_property
    def freedoms_flame_primary(self) -> List[str]:
        return [
            "SG-451 Cookout",
            "FLAM-66 Torcher"
        ]
    
    @functools.cached_property
    def freedoms_flame_secondary(self) -> List[str]:
        return ["P-72 Crisper"]
    
    @functools.cached_property
    def freedoms_flame_booster(self) -> List[str]:
        return ["Firebomb Hellpods"]
    
    @functools.cached_property
    def freedoms_flame_armor(self) -> List[str]:
        return [
            "I-09 Heatseeker",
            "I-102 Draconaught"
        ]
    
    @functools.cached_property
    def chemical_agents_secondary(self) -> List[str]:
        return ["P-11 Stim Pistol"]
    
    @functools.cached_property
    def chemical_agents_trowable(self) -> List[str]:
        return ["G-4 Gas"]
    
    @functools.cached_property
    def chemical_agents_stratagems(self) -> List[str]:
        return [
            "TX-41 Sterilizer",
            'AX/TX-13 "Guard Dog" Dog Breath'
        ]
    
    @functools.cached_property
    def chemical_agents_armor(self) -> List[str]:
        return [
            "AF-50 Noxious Ranger",
            "AF-02 Haz-Master"
        ]
    
    @functools.cached_property
    def truth_enforcers_primary(self) -> List[str]:
        return [
            "SG-20 Halt",
            "SMG-32 Reprimand"
        ]
    
    @functools.cached_property
    def truth_enforcers_secondary(self) -> List[str]:
        return ["PLAS-15 Loyalist"]
    
    @functools.cached_property
    def truth_enforcers_booster(self) -> List[str]:
        return ["Dead Sprint"]
    
    @functools.cached_property
    def truth_enforcers_armor(self) -> List[str]:
        return [
            "UF-50 Bloodhound",
            "UF-16 Inspector"
        ]
    
    @functools.cached_property
    def urban_legends_secondary(self) -> List[str]:
        return ["CQC-19 Stun Lance"]
    
    @functools.cached_property
    def urban_legends_booster(self) -> List[str]:
        return ["Armed Resuply Pods"]
    
    @functools.cached_property
    def urban_legends_stratagems(self) -> List[str]:
        return [
            "SH-51 Directional Shield",
            "A/FLAM-40 Flame Sentry",
            "E/AT-12 Anti-Tank Emplacement"
        ]
    
    @functools.cached_property
    def urban_legends_armor(self) -> List[str]:
        return [
            "SR-24 Street Scout",
            "SR-18 Roadblock"
        ]
    
    @functools.cached_property
    def servants_of_freedom_primary(self) -> List[str]:
        return ["LAS-17 Double-Edge Sickle"]
    
    @functools.cached_property
    def servants_of_freedom_secondary(self) -> List[str]:
        return ["GP-20 Ultimatum"]
    
    @functools.cached_property
    def servants_of_freedom_trowable(self) -> List[str]:
        return ["G-50 Seeker"]
    
    @functools.cached_property
    def servants_of_freedom_stratagems(self) -> List[str]:
        return ["B-100 Portable Hellbomb"]
    
    @functools.cached_property
    def servants_of_freedom_armor(self) -> List[str]:
        return [
            "IE-3 Martyr",
            "IE-12 Righteous"
        ]
    
    @functools.cached_property
    def borderline_justice_primary(self) -> List[str]:
        return ["R-6 Deadeye"]
    
    @functools.cached_property
    def borderline_justice_secondary(self) -> List[str]:
        return ["LAS-58 Talon"]
    
    @functools.cached_property
    def borderline_justice_trowable(self) -> List[str]:
        return ["TED-63 Dynamite"]
    
    @functools.cached_property
    def borderline_justice_booster(self) -> List[str]:
        return ["Sample Extradicator"]
    
    @functools.cached_property
    def borderline_justice_stratagems(self) -> List[str]:
        return ["LIFT-860 Hover Pack"]
    
    @functools.cached_property
    def borderline_justice_armor(self) -> List[str]:
        return [
            "GS-17 Frontier Marshal",
            "GS-66 Lawmaker"
        ]
    
    @functools.cached_property
    def masters_of_ceremony_primary(self) -> List[str]:
        return ["R-2 Amendment"]
    
    @functools.cached_property
    def masters_of_ceremony_secondary(self) -> List[str]:
        return ["CQC-2 Saber"]
    
    @functools.cached_property
    def masters_of_ceremony_trowable(self) -> List[str]:
        return ["G-142 Pyrotech"]
    
    @functools.cached_property
    def masters_of_ceremony_booster(self) -> List[str]:
        return ["Sample Scanner"]
    
    @functools.cached_property
    def masters_of_ceremony_stratagems(self) -> List[str]:
        return ["CQC-1 One True Flag"]
    
    @functools.cached_property
    def masters_of_ceremony_armor(self) -> List[str]:
        return [
            "RE-2310 Honorary Guard",
            "RE-1861 Parade Commander"
        ]
    
    @functools.cached_property
    def force_of_law_primary(self) -> List[str]:
        return ["AR-32 Pacifier"]
    
    @functools.cached_property
    def force_of_law_trowable(self) -> List[str]:
        return ["G-109 Urchin"]
    
    @functools.cached_property
    def force_of_law_booster(self) -> List[str]:
        return ["Stun Pods"]
    
    @functools.cached_property
    def force_of_law_stratagems(self) -> List[str]:
        return [
            "GL-52 De-Escalator",
            'AX/ARC-3 "Guard Dog" K-9'
        ]
    
    @functools.cached_property
    def force_of_law_armor(self) -> List[str]:
        return [
            "BP-20 Correct Officer",
            "BP-32 Jackboot"
        ]
    
    @functools.cached_property
    def control_group_primary(self) -> List[str]:
        return ["VG-70 Variable"]
    
    @functools.cached_property
    def control_group_throwable(self) -> List[str]:
        return ["G-31 Arc"]
    
    @functools.cached_property
    def control_group_stratagems(self) -> List[str]:
        return [
            "PLAS-45 Epoch",
            "A/LAS-98 Laser Sentry",
            "LIFT-182 Warp Pack"
        ]
    
    @functools.cached_property
    def control_group_armor(self) -> List[str]:
        return [
            "AD-26 Bleeding Edge",
            "AD-49 Apollonian"
        ]
    
    @functools.cached_property
    def halo_odst_primary(self) -> List[str]:
        return [
            "MA5C Assault Rifle",
            "M7S SMG",
            "M90A Shotgun"
        ]
    
    @functools.cached_property
    def halo_odst_secondary(self) -> List[str]:
        return ["M6C/SOCOM Pistol"]
    
    @functools.cached_property
    def halo_odst_armor(self) -> List[str]:
        return [
            "A-9 Helljumper",
            "A-35 Recon"
        ]
    
    def primary_weapons(self) -> List[str]:
        primary = self.primary_base[:]
        primary.extend(self.archipelago_options.helldivers_2_superstore_primary.value)
        if self.include_super_citizens:
            primary.extend(self.super_citizen_primary)
        if self.has_helldivers_movilize:
            primary.extend(self.helldivers_movilize_primary)
        if self.has_steeled_veterans:
            primary.extend(self.steeled_veterans_primary)
        if self.has_cutting_edge:
            primary.extend(self.cutting_edge_primary)
        if self.has_democratic_detonation:
            primary.extend(self.democratic_detonation_primary)
        if self.has_polar_patriots:
            primary.extend(self.polar_patriots_primary)
        if self.has_viper_commandos:
            primary.extend(self.viper_commandos_primary)
        if self.has_freedoms_flame:
            primary.extend(self.freedoms_flame_primary)
        if self.has_truth_enforcers:
            primary.extend(self.truth_enforcers_primary)
        if self.has_servants_of_freedom:
            primary.extend(self.servants_of_freedom_primary)
        if self.has_borderline_justice:
            primary.extend(self.borderline_justice_primary)
        if self.has_masters_of_ceremony:
            primary.extend(self.masters_of_ceremony_primary)
        if self.has_force_of_law:
            primary.extend(self.force_of_law_primary)
        if self.has_control_group:
            primary.extend(self.control_group_primary)
        if self.has_halo_odst:
            primary.extend(self.halo_odst_primary)
        return sorted(primary)
    
    def secondary_weapons(self) -> List[str]:
        secondary = self.secondary_base[:]
        secondary.extend(self.archipelago_options.helldivers_2_superstore_secondary.value)
        if self.has_helldivers_movilize:
            secondary.extend(self.helldivers_movilize_secondary)
        if self.has_steeled_veterans:
            secondary.extend(self.steeled_veterans_secondary)
        if self.has_cutting_edge:
            secondary.extend(self.cutting_edge_secondary)
        if self.has_democratic_detonation:
            secondary.extend(self.democratic_detonation_secondary)
        if self.has_polar_patriots:
            secondary.extend(self.polar_patriots_secondary)
        if self.has_viper_commandos:
            secondary.extend(self.viper_commandos_secondary)
        if self.has_freedoms_flame:
            secondary.extend(self.freedoms_flame_secondary)
        if self.has_chemical_agents:
            secondary.extend(self.chemical_agents_secondary)
        if self.has_truth_enforcers:
            secondary.extend(self.truth_enforcers_secondary)
        if self.has_urban_legends:
            secondary.extend(self.urban_legends_secondary)
        if self.has_servants_of_freedom:
            secondary.extend(self.servants_of_freedom_secondary)
        if self.has_borderline_justice:
            secondary.extend(self.borderline_justice_secondary)
        if self.has_masters_of_ceremony:
            secondary.extend(self.masters_of_ceremony_secondary)
        if self.has_halo_odst:
            secondary.extend(self.halo_odst_secondary)
        return sorted(secondary)
    
    def trowable(self) -> List[str]:
        trowable = self.trowable_base[:]
        if self.has_helldivers_movilize:
            trowable.extend(self.helldivers_movilize_trowable)
        if self.has_steeled_veterans:
            trowable.extend(self.steeled_veterans_trowable)
        if self.has_cutting_edge:
            trowable.extend(self.cutting_edge_trowable)
        if self.has_democratic_detonation:
            trowable.extend(self.democratic_detonation_trowable)
        if self.has_polar_patriots:
            trowable.extend(self.polar_patriots_trowable)
        if self.has_viper_commandos:
            trowable.extend(self.viper_commandos_trowable)
        if self.has_chemical_agents:
            trowable.extend(self.chemical_agents_trowable)
        if self.has_servants_of_freedom:
            trowable.extend(self.servants_of_freedom_trowable)
        if self.has_borderline_justice:
            trowable.extend(self.borderline_justice_trowable)
        if self.has_masters_of_ceremony:
            trowable.extend(self.masters_of_ceremony_trowable)
        if self.has_force_of_law:
            trowable.extend(self.force_of_law_trowable)
        if self.has_control_group:
            trowable.extend(self.control_group_throwable)
        return sorted(trowable)
    
    def booster(self) -> List[str]:
        booster = []
        if self.has_helldivers_movilize:
            booster.extend(self.helldivers_movilize_booster)
        if self.has_steeled_veterans:
            booster.extend(self.steeled_veterans_booster)
        if self.has_cutting_edge:
            booster.extend(self.cutting_edge_booster)
        if self.has_democratic_detonation:
            booster.extend(self.democratic_detonation_booster)
        if self.has_polar_patriots:
            booster.extend(self.polar_patriots_booster)
        if self.has_viper_commandos:
            booster.extend(self.viper_commandos_booster)
        if self.has_freedoms_flame:
            booster.extend(self.freedoms_flame_booster)
        if self.has_truth_enforcers:
            booster.extend(self.truth_enforcers_booster)
        if self.has_urban_legends:
            booster.extend(self.urban_legends_booster)
        if self.has_borderline_justice:
            booster.extend(self.borderline_justice_booster)
        if self.has_masters_of_ceremony:
            booster.extend(self.masters_of_ceremony_booster)
        if self.has_force_of_law:
            booster.extend(self.force_of_law_booster)
        if not booster:
            return "No booster"
        return sorted(booster)
    
    def stratagems(self) -> List[str]:
        stratagem = self.stratagem_base[:]
        if self.has_chemical_agents:
            stratagem.extend(self.chemical_agents_stratagems)
        if self.has_urban_legends:
            stratagem.extend(self.urban_legends_stratagems)
        if self.has_servants_of_freedom:
            stratagem.extend(self.servants_of_freedom_stratagems)
        if self.has_borderline_justice:
            stratagem.extend(self.borderline_justice_stratagems)
        if self.has_masters_of_ceremony:
            stratagem.extend(self.masters_of_ceremony_stratagems)
        if self.has_force_of_law:
            stratagem.extend(self.force_of_law_stratagems)
        if self.has_control_group:
            stratagem.extend(self.control_group_stratagems)
        return sorted(stratagem)
    
    def armor(self) -> List[str]:
        armor = self.armor_base[:]
        armor.extend(self.archipelago_options.helldivers_2_superstore_armors.value)
        if self.include_super_citizens:
            armor.extend(self.super_citizen_armor)
        if self.has_helldivers_movilize:
            armor.extend(self.helldivers_movilize_armor)
        if self.has_steeled_veterans:
            armor.extend(self.steeled_veterans_armor)
        if self.has_cutting_edge:
            armor.extend(self.cutting_edge_armor)
        if self.has_democratic_detonation:
            armor.extend(self.democratic_detonation_armor)
        if self.has_polar_patriots:
            armor.extend(self.polar_patriots_armor)
        if self.has_viper_commandos:
            armor.extend(self.viper_commandos_armor)
        if self.has_freedoms_flame:
            armor.extend(self.freedoms_flame_armor)
        if self.has_chemical_agents:
            armor.extend(self.chemical_agents_armor)
        if self.has_truth_enforcers:
            armor.extend(self.truth_enforcers_armor)
        if self.has_urban_legends:
            armor.extend(self.urban_legends_armor)
        if self.has_servants_of_freedom:
            armor.extend(self.servants_of_freedom_armor)
        if self.has_borderline_justice:
            armor.extend(self.borderline_justice_armor)
        if self.has_masters_of_ceremony:
            armor.extend(self.masters_of_ceremony_armor)
        if self.has_force_of_law:
            armor.extend(self.force_of_law_armor)
        if self.has_control_group:
            armor.extend(self.control_group_armor)
        if self.has_halo_odst:
            armor.extend(self.halo_odst_armor)
        return sorted(armor)

#archipelago options
class warbonds(OptionSet):
    '''
    The warbonds the player has access to. (Asumes the player has all the content whithin the warbond unlocked)
    '''
    display_name = "Heldivers 2 Warbonds Owned"
    valid_keys = [
        "Helldivers Movilize",
        "Steeled Veterans",
        "Cutting Edge",
        "Democratic Detonation",
        "Polar Patriots",
        "Viper Commandos",
        "Freedom's Flame",
        "Chemical Agents",
        "Truth Enforcers",
        "Urban Legends",
        "Servants of Freedom",
        "Borderline Justice",
        "Masters of Ceremony",
        "Force of Law",
        "Control Group",
        "Halo ODST"
    ]
    default=valid_keys

class super_citizen(Toggle):
    """
    Indicates if the player has the Super Citizen Edition DLC.
    """
    display_name = "Super Citizen Edition"
    default = False

class superstore_primary(OptionSet):
    """
    Indicates wich superstore or limited time primary weapons the player has.
    """
    display_name = "Superstore Primary Weapons"
    valid_keys = [
        "StA-52 Assault Rifle",
        "StA-11 SMG",
        "PLAS-39 Accelerator Rifle"
    ]
    default=valid_keys

class superstore_secondary(OptionSet):
    """
    Indicates wich superstore or limited time secondary weapons the player has.
    """
    display_name = "Superstore Secondary Weapons"
    valid_keys = [
        "CQC-30 Stun Baton",
        "CQC-5 Combat Hatchet"
    ]
    default=valid_keys

class superstore_armor(OptionSet):
    """
    Indicates wich superstore or limited time armors the player has.
    """
    display_name = "Superstore Armors"
    valid_keys = [
        "SC-37 Legionnaire",
        "CE-74 Breaker",
        "FS-38 Eradicator",
        "B-08 Light Gunner",
        "CM-21 Trench Paramedic",
        "CE-67 Titan",
        "FS-37 Ravager",
        "AC-2 Obedient",
        "IE-57 Hell-Bent",
        "GS-11 Democracy's Deputy",
        "AD-11 Livewire",
        "TR-7 Ambassador of the Brand",
        "TR-9 Cavalier of Democracy",
        "SC-15 Drone Master",
        "B-24 Enforcer",
        "CE-81 Juggernaut",
        "FS-34 Exterminator",
        "CM-10 Clinician",
        "CW-9 White Wolf",
        "PH-56 Jaguar",
        "I-92 Fire Fighter",
        "AF-91 Field Chemist",
        "UF-84 Doubt Killer",
        "AC-1 Dutiful",
        "B-22 Model Citizen",
        "TR-62 Knight",
        "B-27 Fortified Commando",
        "FS-61 Dreadnought",
        "FS-11 Executioner",
        "CM-17 Butcher",
        "CE-64 Grenadier",
        "CE-101 Guerilla Gorilla",
        "I-44 Salamander",
        "AF-52 Lockdown",
        "SR-64 Cinderblock",
        "RE-824 Bearar of the Standard",
        "BP-77 Grand Juror"
    ]
    default=valid_keys
